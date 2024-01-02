import { Arguments } from 'yargs';
import { randomBytes } from 'crypto';
import { ECPairInterface } from 'ecpair';
import { Network, Transaction } from 'bitcoinjs-lib';
import { LiquidRefundDetails } from 'boltz-core/lib/liquid';
import {
  detectSwap,
  Musig,
  OutputType,
  RefundDetails,
  SwapTreeSerializer,
  TaprootUtils,
  Types,
} from 'boltz-core';
import { Network as LiquidNetwork } from 'liquidjs-lib/src/networks';
import { Transaction as LiquidTransaction } from 'liquidjs-lib/src/transaction';
import { TaprootUtils as LiquidTaprootDetails } from 'boltz-core/dist/lib/liquid';
import { getHexBuffer } from '../Utils';
import { ECPair } from '../ECPairHelper';
import { CurrencyType } from '../consts/Enums';
import { PartialSignature } from './BoltzApiClient';
import {
  constructClaimTransaction,
  setup,
  tweakMusig,
  zkpMusig,
} from '../Core';
import {
  currencyTypeFromNetwork,
  getWalletStub,
  parseNetwork,
} from './Command';

export const setupCooperativeTransaction = async (
  argv: Arguments<any>,
  keyExtractionFunc: (tree: Types.SwapTree) => Buffer,
) => {
  await setup();

  const network = parseNetwork(argv.network);
  const currencyType = currencyTypeFromNetwork(argv.network);

  const swapTree = SwapTreeSerializer.deserializeSwapTree(argv.swapTree);
  const keys = ECPair.fromPrivateKey(getHexBuffer(argv.privateKey));
  const theirPublicKey = keyExtractionFunc(swapTree);

  const musig = new Musig(zkpMusig, keys, randomBytes(32), [
    theirPublicKey,
    keys.publicKey,
  ]);
  const tweakedKey = tweakMusig(currencyType, musig, swapTree);

  return {
    keys,
    musig,
    network,
    tweakedKey,
    currencyType,
    theirPublicKey,
  };
};

export const prepareCooperativeTransaction = <
  T extends Transaction | LiquidTransaction,
>(
  argv: Arguments<any>,
  network: Network | LiquidNetwork,
  currencyType: CurrencyType,
  keys: ECPairInterface,
  tweakedKey: Buffer,
  lockupTx: T,
): { tx: T; details: RefundDetails | LiquidRefundDetails } => {
  const swapOutput = detectSwap(tweakedKey, lockupTx);
  if (swapOutput === undefined) {
    throw 'could not find swap output';
  }

  const details = {
    ...swapOutput,
    keys,
    txHash: lockupTx.getHash(),
    type: OutputType.Taproot,
    cooperative: true,
  } as any;
  const tx = constructClaimTransaction(
    getWalletStub(
      currencyType,
      network,
      argv.destinationAddress,
      argv.blindingKey,
    ),
    [details],
    argv.destinationAddress,
    argv.feePerVbyte,
  );

  return {
    details,
    tx: tx as T,
  };
};

export const finalizeCooperativeTransaction = <
  T extends Transaction | LiquidTransaction,
>(
  tx: T,
  musig: Musig,
  network: Network | LiquidNetwork,
  currencyType: CurrencyType,
  otherPublicKey: Buffer,
  details: RefundDetails | LiquidRefundDetails,
  partialSig: PartialSignature,
): T => {
  musig.aggregateNonces([[otherPublicKey, getHexBuffer(partialSig.pubNonce)]]);

  let hash: Buffer;
  if (currencyType === CurrencyType.BitcoinLike) {
    hash = TaprootUtils.hashForWitnessV1(
      [details] as RefundDetails[],
      tx as Transaction,
      0,
    );
  } else {
    hash = LiquidTaprootDetails.hashForWitnessV1(
      network as LiquidNetwork,
      [details] as LiquidRefundDetails[],
      tx as LiquidTransaction,
      0,
    );
  }

  musig.initializeSession(hash);
  musig.signPartial();
  musig.addPartial(otherPublicKey, getHexBuffer(partialSig.partialSignature));
  tx.setWitness(0, [musig.aggregatePartials()]);

  return tx;
};

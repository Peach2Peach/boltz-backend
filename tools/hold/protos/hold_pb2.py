# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hold.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\nhold.proto\x12\x04hold"\x10\n\x0eGetInfoRequest""\n\x0fGetInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t"\xed\x01\n\x0eInvoiceRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\x12\x13\n\x0b\x61mount_msat\x18\x02 \x01(\x04\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x65xpiry\x18\x04 \x01(\x04H\x01\x88\x01\x01\x12"\n\x15min_final_cltv_expiry\x18\x05 \x01(\x04H\x02\x88\x01\x01\x12(\n\rrouting_hints\x18\x06 \x03(\x0b\x32\x11.hold.RoutingHintB\x0e\n\x0c_descriptionB\t\n\x07_expiryB\x18\n\x16_min_final_cltv_expiry"!\n\x0fInvoiceResponse\x12\x0e\n\x06\x62olt11\x18\x01 \x01(\t"#\n\x13RoutingHintsRequest\x12\x0c\n\x04node\x18\x01 \x01(\t"q\n\x03Hop\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x18\n\x10short_channel_id\x18\x02 \x01(\t\x12\x10\n\x08\x62\x61se_fee\x18\x03 \x01(\x04\x12\x0f\n\x07ppm_fee\x18\x04 \x01(\x04\x12\x19\n\x11\x63ltv_expiry_delta\x18\x05 \x01(\x04"&\n\x0bRoutingHint\x12\x17\n\x04hops\x18\x01 \x03(\x0b\x32\t.hold.Hop"8\n\x14RoutingHintsResponse\x12 \n\x05hints\x18\x01 \x03(\x0b\x32\x11.hold.RoutingHint"9\n\x0bListRequest\x12\x19\n\x0cpayment_hash\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_payment_hash"H\n\x04Htlc\x12\x1e\n\x05state\x18\x01 \x01(\x0e\x32\x0f.hold.HtlcState\x12\x0c\n\x04msat\x18\x02 \x01(\x04\x12\x12\n\ncreated_at\x18\x03 \x01(\x04"\xb5\x01\n\x07Invoice\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\x12\x1d\n\x10payment_preimage\x18\x02 \x01(\tH\x00\x88\x01\x01\x12!\n\x05state\x18\x03 \x01(\x0e\x32\x12.hold.InvoiceState\x12\x0e\n\x06\x62olt11\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\x04\x12\x19\n\x05htlcs\x18\x06 \x03(\x0b\x32\n.hold.HtlcB\x13\n\x11_payment_preimage"/\n\x0cListResponse\x12\x1f\n\x08invoices\x18\x01 \x03(\x0b\x32\r.hold.Invoice")\n\rSettleRequest\x12\x18\n\x10payment_preimage\x18\x01 \x01(\t"\x10\n\x0eSettleResponse"%\n\rCancelRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t"\x10\n\x0e\x43\x61ncelResponse"$\n\x0cTrackRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t"2\n\rTrackResponse\x12!\n\x05state\x18\x01 \x01(\x0e\x32\x12.hold.InvoiceState"\x11\n\x0fTrackAllRequest"[\n\x10TrackAllResponse\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\x12\x0e\n\x06\x62olt11\x18\x02 \x01(\t\x12!\n\x05state\x18\x03 \x01(\x0e\x32\x12.hold.InvoiceState"2\n\x10PayStatusRequest\x12\x13\n\x06\x62olt11\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_bolt11"\x94\x07\n\x11PayStatusResponse\x12\x31\n\x06status\x18\x01 \x03(\x0b\x32!.hold.PayStatusResponse.PayStatus\x1a\xcb\x06\n\tPayStatus\x12\x0e\n\x06\x62olt11\x18\x01 \x01(\t\x12\x13\n\x0b\x61mount_msat\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\x12;\n\x08\x61ttempts\x18\x04 \x03(\x0b\x32).hold.PayStatusResponse.PayStatus.Attempt\x1a\xc6\x05\n\x07\x41ttempt\x12\x10\n\x08strategy\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x04\x12\x16\n\x0e\x61ge_in_seconds\x18\x03 \x01(\x04\x12\x15\n\x08\x65nd_time\x18\x04 \x01(\x04H\x00\x88\x01\x01\x12\x45\n\x05state\x18\x05 \x01(\x0e\x32\x36.hold.PayStatusResponse.PayStatus.Attempt.AttemptState\x12G\n\x07success\x18\x06 \x01(\x0b\x32\x31.hold.PayStatusResponse.PayStatus.Attempt.SuccessH\x01\x88\x01\x01\x12G\n\x07\x66\x61ilure\x18\x07 \x01(\x0b\x32\x31.hold.PayStatusResponse.PayStatus.Attempt.FailureH\x02\x88\x01\x01\x1a/\n\x07Success\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x18\n\x10payment_preimage\x18\x02 \x01(\t\x1a\xfa\x01\n\x07\x46\x61ilure\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x04\x12I\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x36.hold.PayStatusResponse.PayStatus.Attempt.Failure.DataH\x00\x88\x01\x01\x1a|\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x13\n\x0braw_message\x18\x02 \x01(\t\x12\x11\n\tfail_code\x18\x03 \x01(\x04\x12\x15\n\rfail_codename\x18\x04 \x01(\t\x12\x14\n\x0c\x65rring_index\x18\x05 \x01(\x04\x12\x13\n\x0b\x65rring_node\x18\x06 \x01(\tB\x07\n\x05_data":\n\x0c\x41ttemptState\x12\x13\n\x0f\x41TTEMPT_PENDING\x10\x00\x12\x15\n\x11\x41TTEMPT_COMPLETED\x10\x01\x42\x0b\n\t_end_timeB\n\n\x08_successB\n\n\x08_failure*a\n\x0cInvoiceState\x12\x12\n\x0eINVOICE_UNPAID\x10\x00\x12\x14\n\x10INVOICE_ACCEPTED\x10\x01\x12\x10\n\x0cINVOICE_PAID\x10\x02\x12\x15\n\x11INVOICE_CANCELLED\x10\x03*D\n\tHtlcState\x12\x11\n\rHTLC_ACCEPTED\x10\x00\x12\x10\n\x0cHTLC_SETTLED\x10\x01\x12\x12\n\x0eHTLC_CANCELLED\x10\x02\x32\x97\x04\n\x04Hold\x12\x38\n\x07GetInfo\x12\x14.hold.GetInfoRequest\x1a\x15.hold.GetInfoResponse"\x00\x12\x38\n\x07Invoice\x12\x14.hold.InvoiceRequest\x1a\x15.hold.InvoiceResponse"\x00\x12G\n\x0cRoutingHints\x12\x19.hold.RoutingHintsRequest\x1a\x1a.hold.RoutingHintsResponse"\x00\x12/\n\x04List\x12\x11.hold.ListRequest\x1a\x12.hold.ListResponse"\x00\x12\x35\n\x06Settle\x12\x13.hold.SettleRequest\x1a\x14.hold.SettleResponse"\x00\x12\x35\n\x06\x43\x61ncel\x12\x13.hold.CancelRequest\x1a\x14.hold.CancelResponse"\x00\x12\x34\n\x05Track\x12\x12.hold.TrackRequest\x1a\x13.hold.TrackResponse"\x00\x30\x01\x12=\n\x08TrackAll\x12\x15.hold.TrackAllRequest\x1a\x16.hold.TrackAllResponse"\x00\x30\x01\x12>\n\tPayStatus\x12\x16.hold.PayStatusRequest\x1a\x17.hold.PayStatusResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "hold_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_INVOICESTATE"]._serialized_start = 2256
    _globals["_INVOICESTATE"]._serialized_end = 2353
    _globals["_HTLCSTATE"]._serialized_start = 2355
    _globals["_HTLCSTATE"]._serialized_end = 2423
    _globals["_GETINFOREQUEST"]._serialized_start = 20
    _globals["_GETINFOREQUEST"]._serialized_end = 36
    _globals["_GETINFORESPONSE"]._serialized_start = 38
    _globals["_GETINFORESPONSE"]._serialized_end = 72
    _globals["_INVOICEREQUEST"]._serialized_start = 75
    _globals["_INVOICEREQUEST"]._serialized_end = 312
    _globals["_INVOICERESPONSE"]._serialized_start = 314
    _globals["_INVOICERESPONSE"]._serialized_end = 347
    _globals["_ROUTINGHINTSREQUEST"]._serialized_start = 349
    _globals["_ROUTINGHINTSREQUEST"]._serialized_end = 384
    _globals["_HOP"]._serialized_start = 386
    _globals["_HOP"]._serialized_end = 499
    _globals["_ROUTINGHINT"]._serialized_start = 501
    _globals["_ROUTINGHINT"]._serialized_end = 539
    _globals["_ROUTINGHINTSRESPONSE"]._serialized_start = 541
    _globals["_ROUTINGHINTSRESPONSE"]._serialized_end = 597
    _globals["_LISTREQUEST"]._serialized_start = 599
    _globals["_LISTREQUEST"]._serialized_end = 656
    _globals["_HTLC"]._serialized_start = 658
    _globals["_HTLC"]._serialized_end = 730
    _globals["_INVOICE"]._serialized_start = 733
    _globals["_INVOICE"]._serialized_end = 914
    _globals["_LISTRESPONSE"]._serialized_start = 916
    _globals["_LISTRESPONSE"]._serialized_end = 963
    _globals["_SETTLEREQUEST"]._serialized_start = 965
    _globals["_SETTLEREQUEST"]._serialized_end = 1006
    _globals["_SETTLERESPONSE"]._serialized_start = 1008
    _globals["_SETTLERESPONSE"]._serialized_end = 1024
    _globals["_CANCELREQUEST"]._serialized_start = 1026
    _globals["_CANCELREQUEST"]._serialized_end = 1063
    _globals["_CANCELRESPONSE"]._serialized_start = 1065
    _globals["_CANCELRESPONSE"]._serialized_end = 1081
    _globals["_TRACKREQUEST"]._serialized_start = 1083
    _globals["_TRACKREQUEST"]._serialized_end = 1119
    _globals["_TRACKRESPONSE"]._serialized_start = 1121
    _globals["_TRACKRESPONSE"]._serialized_end = 1171
    _globals["_TRACKALLREQUEST"]._serialized_start = 1173
    _globals["_TRACKALLREQUEST"]._serialized_end = 1190
    _globals["_TRACKALLRESPONSE"]._serialized_start = 1192
    _globals["_TRACKALLRESPONSE"]._serialized_end = 1283
    _globals["_PAYSTATUSREQUEST"]._serialized_start = 1285
    _globals["_PAYSTATUSREQUEST"]._serialized_end = 1335
    _globals["_PAYSTATUSRESPONSE"]._serialized_start = 1338
    _globals["_PAYSTATUSRESPONSE"]._serialized_end = 2254
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS"]._serialized_start = 1411
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS"]._serialized_end = 2254
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT"]._serialized_start = 1544
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT"]._serialized_end = 2254
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_SUCCESS"]._serialized_start = 1857
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_SUCCESS"]._serialized_end = 1904
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_FAILURE"]._serialized_start = 1907
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_FAILURE"]._serialized_end = 2157
    _globals[
        "_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_FAILURE_DATA"
    ]._serialized_start = 2024
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_FAILURE_DATA"]._serialized_end = 2148
    _globals[
        "_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_ATTEMPTSTATE"
    ]._serialized_start = 2159
    _globals["_PAYSTATUSRESPONSE_PAYSTATUS_ATTEMPT_ATTEMPTSTATE"]._serialized_end = 2217
    _globals["_HOLD"]._serialized_start = 2426
    _globals["_HOLD"]._serialized_end = 2961
# @@protoc_insertion_point(module_scope)

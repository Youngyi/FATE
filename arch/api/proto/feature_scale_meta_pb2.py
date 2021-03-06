# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-scale-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature-scale-meta.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_pb=_b('\n\x18\x66\x65\x61ture-scale-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xdb\x02\n\tScaleMeta\x12\x10\n\x08is_scale\x18\x01 \x01(\x08\x12\x10\n\x08strategy\x18\x02 \x01(\t\x12\x61\n\x11minmax_scale_meta\x18\x03 \x03(\x0b\x32\x46.com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.MinmaxScaleMetaEntry\x12V\n\x13standard_scale_meta\x18\x04 \x01(\x0b\x32\x39.com.webank.ai.fate.core.mlmodel.buffer.StandardScaleMeta\x1ao\n\x14MinmaxScaleMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta:\x02\x38\x01\"_\n\x0fMinMaxScaleMeta\x12\x12\n\nfeat_upper\x18\x05 \x01(\t\x12\x12\n\nfeat_lower\x18\x06 \x01(\t\x12\x11\n\tout_upper\x18\x07 \x01(\t\x12\x11\n\tout_lower\x18\x08 \x01(\t\"8\n\x11StandardScaleMeta\x12\x11\n\twith_mean\x18\t \x01(\x08\x12\x10\n\x08with_std\x18\n \x01(\x08\x42\x10\x42\x0eScaleMetaProtob\x06proto3')
)




_SCALEMETA_MINMAXSCALEMETAENTRY = _descriptor.Descriptor(
  name='MinmaxScaleMetaEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.MinmaxScaleMetaEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.MinmaxScaleMetaEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.MinmaxScaleMetaEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=416,
)

_SCALEMETA = _descriptor.Descriptor(
  name='ScaleMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_scale', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.is_scale', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.strategy', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minmax_scale_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.minmax_scale_meta', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='standard_scale_meta', full_name='com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.standard_scale_meta', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SCALEMETA_MINMAXSCALEMETAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=416,
)


_MINMAXSCALEMETA = _descriptor.Descriptor(
  name='MinMaxScaleMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feat_upper', full_name='com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta.feat_upper', index=0,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feat_lower', full_name='com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta.feat_lower', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_upper', full_name='com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta.out_upper', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_lower', full_name='com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta.out_lower', index=3,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=513,
)


_STANDARDSCALEMETA = _descriptor.Descriptor(
  name='StandardScaleMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.StandardScaleMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='with_mean', full_name='com.webank.ai.fate.core.mlmodel.buffer.StandardScaleMeta.with_mean', index=0,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_std', full_name='com.webank.ai.fate.core.mlmodel.buffer.StandardScaleMeta.with_std', index=1,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=571,
)

_SCALEMETA_MINMAXSCALEMETAENTRY.fields_by_name['value'].message_type = _MINMAXSCALEMETA
_SCALEMETA_MINMAXSCALEMETAENTRY.containing_type = _SCALEMETA
_SCALEMETA.fields_by_name['minmax_scale_meta'].message_type = _SCALEMETA_MINMAXSCALEMETAENTRY
_SCALEMETA.fields_by_name['standard_scale_meta'].message_type = _STANDARDSCALEMETA
DESCRIPTOR.message_types_by_name['ScaleMeta'] = _SCALEMETA
DESCRIPTOR.message_types_by_name['MinMaxScaleMeta'] = _MINMAXSCALEMETA
DESCRIPTOR.message_types_by_name['StandardScaleMeta'] = _STANDARDSCALEMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScaleMeta = _reflection.GeneratedProtocolMessageType('ScaleMeta', (_message.Message,), dict(

  MinmaxScaleMetaEntry = _reflection.GeneratedProtocolMessageType('MinmaxScaleMetaEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCALEMETA_MINMAXSCALEMETAENTRY,
    __module__ = 'feature_scale_meta_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta.MinmaxScaleMetaEntry)
    ))
  ,
  DESCRIPTOR = _SCALEMETA,
  __module__ = 'feature_scale_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ScaleMeta)
  ))
_sym_db.RegisterMessage(ScaleMeta)
_sym_db.RegisterMessage(ScaleMeta.MinmaxScaleMetaEntry)

MinMaxScaleMeta = _reflection.GeneratedProtocolMessageType('MinMaxScaleMeta', (_message.Message,), dict(
  DESCRIPTOR = _MINMAXSCALEMETA,
  __module__ = 'feature_scale_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.MinMaxScaleMeta)
  ))
_sym_db.RegisterMessage(MinMaxScaleMeta)

StandardScaleMeta = _reflection.GeneratedProtocolMessageType('StandardScaleMeta', (_message.Message,), dict(
  DESCRIPTOR = _STANDARDSCALEMETA,
  __module__ = 'feature_scale_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.StandardScaleMeta)
  ))
_sym_db.RegisterMessage(StandardScaleMeta)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\016ScaleMetaProto'))
_SCALEMETA_MINMAXSCALEMETAENTRY.has_options = True
_SCALEMETA_MINMAXSCALEMETAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)

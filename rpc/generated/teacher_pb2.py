# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: teacher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rteacher.proto\x1a\x19google/protobuf/any.proto\" \n\x12TeacherByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x18\n\x08WorkUnit\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xa0\x01\n\x07Teacher\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\t\x12\x12\n\nspecialize\x18\x03 \x01(\t\x12\x14\n\x0cwork_unit_id\x18\x04 \x01(\t\x12 \n\twork_unit\x18\x05 \x01(\x0b\x32\r.Teacher.Unit\x1a \n\x04Unit\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xbe\x01\n\x0fTeacherResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x15\n\rresponse_time\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x13\n\x06\x65rrors\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x08.TeacherH\x01\x88\x01\x01\x12\x0c\n\x04\x63ode\x18\x06 \x01(\x05\x12\x13\n\x06status\x18\x07 \x01(\x08H\x02\x88\x01\x01\x42\t\n\x07_errorsB\x07\n\x05_dataB\t\n\x07_status2I\n\x11TeacherController\x12\x34\n\x0bTeacherById\x12\x13.TeacherByIdRequest\x1a\x10.TeacherResponseb\x06proto3')



_TEACHERBYIDREQUEST = DESCRIPTOR.message_types_by_name['TeacherByIdRequest']
_WORKUNIT = DESCRIPTOR.message_types_by_name['WorkUnit']
_TEACHER = DESCRIPTOR.message_types_by_name['Teacher']
_TEACHER_UNIT = _TEACHER.nested_types_by_name['Unit']
_TEACHERRESPONSE = DESCRIPTOR.message_types_by_name['TeacherResponse']
TeacherByIdRequest = _reflection.GeneratedProtocolMessageType('TeacherByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEACHERBYIDREQUEST,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:TeacherByIdRequest)
  })
_sym_db.RegisterMessage(TeacherByIdRequest)

WorkUnit = _reflection.GeneratedProtocolMessageType('WorkUnit', (_message.Message,), {
  'DESCRIPTOR' : _WORKUNIT,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:WorkUnit)
  })
_sym_db.RegisterMessage(WorkUnit)

Teacher = _reflection.GeneratedProtocolMessageType('Teacher', (_message.Message,), {

  'Unit' : _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), {
    'DESCRIPTOR' : _TEACHER_UNIT,
    '__module__' : 'teacher_pb2'
    # @@protoc_insertion_point(class_scope:Teacher.Unit)
    })
  ,
  'DESCRIPTOR' : _TEACHER,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:Teacher)
  })
_sym_db.RegisterMessage(Teacher)
_sym_db.RegisterMessage(Teacher.Unit)

TeacherResponse = _reflection.GeneratedProtocolMessageType('TeacherResponse', (_message.Message,), {
  'DESCRIPTOR' : _TEACHERRESPONSE,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:TeacherResponse)
  })
_sym_db.RegisterMessage(TeacherResponse)

_TEACHERCONTROLLER = DESCRIPTOR.services_by_name['TeacherController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TEACHERBYIDREQUEST._serialized_start=44
  _TEACHERBYIDREQUEST._serialized_end=76
  _WORKUNIT._serialized_start=78
  _WORKUNIT._serialized_end=102
  _TEACHER._serialized_start=105
  _TEACHER._serialized_end=265
  _TEACHER_UNIT._serialized_start=233
  _TEACHER_UNIT._serialized_end=265
  _TEACHERRESPONSE._serialized_start=268
  _TEACHERRESPONSE._serialized_end=458
  _TEACHERCONTROLLER._serialized_start=460
  _TEACHERCONTROLLER._serialized_end=533
# @@protoc_insertion_point(module_scope)

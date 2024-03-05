# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyrcareworld/communicator_objects/agent_info_action_pair.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyrcareworld.communicator_objects import (
    agent_info_pb2 as pyrcareworld_dot_communicator__objects_dot_agent__info__pb2,
)
from pyrcareworld.communicator_objects import (
    agent_action_pb2 as pyrcareworld_dot_communicator__objects_dot_agent__action__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="pyrcareworld/communicator_objects/agent_info_action_pair.proto",
    package="communicator_objects",
    syntax="proto3",
    serialized_pb=_b(
        '\n>pyrcareworld/communicator_objects/agent_info_action_pair.proto\x12\x14\x63ommunicator_objects\x1a\x32pyrcareworld/communicator_objects/agent_info.proto\x1a\x34pyrcareworld/communicator_objects/agent_action.proto"\x91\x01\n\x18\x41gentInfoActionPairProto\x12\x38\n\nagent_info\x18\x01 \x01(\x0b\x32$.communicator_objects.AgentInfoProto\x12;\n\x0b\x61\x63tion_info\x18\x02 \x01(\x0b\x32&.communicator_objects.AgentActionProtoB+\xaa\x02(Robotflow.RFUniverse.CommunicatorObjectsb\x06proto3'
    ),
    dependencies=[
        pyrcareworld_dot_communicator__objects_dot_agent__info__pb2.DESCRIPTOR,
        pyrcareworld_dot_communicator__objects_dot_agent__action__pb2.DESCRIPTOR,
    ],
)


_AGENTINFOACTIONPAIRPROTO = _descriptor.Descriptor(
    name="AgentInfoActionPairProto",
    full_name="communicator_objects.AgentInfoActionPairProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="agent_info",
            full_name="communicator_objects.AgentInfoActionPairProto.agent_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="action_info",
            full_name="communicator_objects.AgentInfoActionPairProto.action_info",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=195,
    serialized_end=340,
)

_AGENTINFOACTIONPAIRPROTO.fields_by_name["agent_info"].message_type = (
    pyrcareworld_dot_communicator__objects_dot_agent__info__pb2._AGENTINFOPROTO
)
_AGENTINFOACTIONPAIRPROTO.fields_by_name["action_info"].message_type = (
    pyrcareworld_dot_communicator__objects_dot_agent__action__pb2._AGENTACTIONPROTO
)
DESCRIPTOR.message_types_by_name["AgentInfoActionPairProto"] = _AGENTINFOACTIONPAIRPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentInfoActionPairProto = _reflection.GeneratedProtocolMessageType(
    "AgentInfoActionPairProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AGENTINFOACTIONPAIRPROTO,
        __module__="pyrcareworld.communicator_objects.agent_info_action_pair_pb2",
        # @@protoc_insertion_point(class_scope:communicator_objects.AgentInfoActionPairProto)
    ),
)
_sym_db.RegisterMessage(AgentInfoActionPairProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b("\252\002(Robotflow.RFUniverse.CommunicatorObjects"),
)
# @@protoc_insertion_point(module_scope)

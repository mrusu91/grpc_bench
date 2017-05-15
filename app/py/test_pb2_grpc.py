# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import test_pb2 as test__pb2


class EventsStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PostEvent = channel.unary_unary(
        '/test.Events/PostEvent',
        request_serializer=test__pb2.Event.SerializeToString,
        response_deserializer=test__pb2.Event.FromString,
        )


class EventsServicer(object):

  def PostEvent(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EventsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PostEvent': grpc.unary_unary_rpc_method_handler(
          servicer.PostEvent,
          request_deserializer=test__pb2.Event.FromString,
          response_serializer=test__pb2.Event.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'test.Events', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
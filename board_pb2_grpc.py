# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import board_pb2 as board__pb2


class BoardStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddAdvert = channel.unary_unary(
        '/board.Board/AddAdvert',
        request_serializer=board__pb2.AddAdvertRequest.SerializeToString,
        response_deserializer=board__pb2.AddAdvertReply.FromString,
        )
    self.GetCountOfAdverts = channel.unary_unary(
        '/board.Board/GetCountOfAdverts',
        request_serializer=board__pb2.GetCountOfAdvertsRequest.SerializeToString,
        response_deserializer=board__pb2.GetCountOfAdvertsReply.FromString,
        )
    self.GetAdverts = channel.unary_unary(
        '/board.Board/GetAdverts',
        request_serializer=board__pb2.GetAdvertsRequest.SerializeToString,
        response_deserializer=board__pb2.GetAdvertsReply.FromString,
        )


class BoardServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddAdvert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCountOfAdverts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAdverts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BoardServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddAdvert': grpc.unary_unary_rpc_method_handler(
          servicer.AddAdvert,
          request_deserializer=board__pb2.AddAdvertRequest.FromString,
          response_serializer=board__pb2.AddAdvertReply.SerializeToString,
      ),
      'GetCountOfAdverts': grpc.unary_unary_rpc_method_handler(
          servicer.GetCountOfAdverts,
          request_deserializer=board__pb2.GetCountOfAdvertsRequest.FromString,
          response_serializer=board__pb2.GetCountOfAdvertsReply.SerializeToString,
      ),
      'GetAdverts': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdverts,
          request_deserializer=board__pb2.GetAdvertsRequest.FromString,
          response_serializer=board__pb2.GetAdvertsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'board.Board', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

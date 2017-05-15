from concurrent import futures
import time

import grpc

import test_pb2
import test_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Events(test_pb2_grpc.EventsServicer):

  def PostEvent(self, request, context):
    return test_pb2.Event(
        id=request.id,
        sport=request.sport,
        category=request.category,
        tournament=request.tournament,
        round=request.round,
        team_a=request.team_a,
        team_b=request.team_b,
        score=request.score,
        state=request.state,
        start_timestamp=request.start_timestamp,
    )


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  test_pb2_grpc.add_EventsServicer_to_server(Events(), server)
  server.add_insecure_port('[::]:12344')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()

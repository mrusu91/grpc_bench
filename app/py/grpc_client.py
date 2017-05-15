import timeit

import grpc

import test_pb2
import test_pb2_grpc

COUNT = 500000


def call(stub):
    response = stub.PostEvent(test_pb2.Event(
        id=1,
        sport='football',
        category='England',
        tournament='Premier League',
        round='32',
        team_a='Chelsea FC',
        team_b='Liverpool FC',
        score='0 - 0',
        state='playing',
        start_timestamp=321321.32,
    ))


def get_stub():
    channel = grpc.insecure_channel('10.2.1.32:12344')
    stub = test_pb2_grpc.EventsStub(channel)
    return stub


if __name__ == '__main__':
    result_sec = timeit.timeit(
        'call(stub)',
        setup='from __main__ import call, get_stub; stub = get_stub()',
        number=COUNT,
    )
    print('Total time %.4f' % result_sec)
    result_usec = result_sec * 1000000
    result_per_call = result_usec / COUNT
    print('%.4f usec per call' % result_per_call)

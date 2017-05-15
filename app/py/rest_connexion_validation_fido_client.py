import timeit

from bravado.client import SwaggerClient
from bravado.fido_client import FidoClient

COUNT = 500000


def get_client():
    config = {
        'validate_responses': True,
        'validate_requests': True,
        'timeout': 1.0,
    }
    return SwaggerClient.from_url(
        'http://10.2.1.32:12345/v0/swagger.json',
        http_client=FidoClient(),
        config=config,
    )

def call(client):
    client.Events.post_events(event=dict(
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
    )).result(timeout=1)


if __name__ == '__main__':
    result_sec = timeit.timeit(
        'call(client)',
        setup='from __main__ import get_client, call; client = get_client();',
        number=COUNT,
    )
    print('Total time %.4f' % result_sec)
    result_usec = result_sec * 1000000
    result_per_call = result_usec / COUNT
    print('%.4f usec per call' % result_per_call)

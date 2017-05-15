import timeit
import httplib
import json


COUNT = 500000


def get_conn():
    conn = httplib.HTTPConnection('10.2.1.32', port=12345, timeout=1)
    return conn


def call(conn):
    data = json.dumps(dict(body=dict(
        id=1,
        sport='football',
        category='england',
        tournament='premier league',
        round='32',
        team_a='chelsea fc',
        team_b='liverpool fc',
        score='0 - 0',
        state='playing',
        start_timestamp=321321.32,
    )))
    headers = {'Content-type': 'application/json'}
    conn.request('POST', '/v0/events', data, headers=headers)
    r = conn.getresponse()
    r.read()
    assert r.status < 300


if __name__ == '__main__':
    result_sec = timeit.timeit(
        'call(conn)',
        setup='from __main__ import get_conn, call; conn = get_conn();',
        number=COUNT,
    )
    print('Total time %.4f' % result_sec)
    result_usec = result_sec * 1000000
    result_per_call = result_usec / COUNT
    print('%.4f usec per call' % result_per_call)

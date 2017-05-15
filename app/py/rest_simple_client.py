import timeit

import requests

COUNT = 500000


def call():
    response = requests.get('http://10.2.1.32:12345/', timeout=1, headers={'Connection':'close'})
    response.raise_for_status()


if __name__ == '__main__':
    result_sec = timeit.timeit(
        'call()',
        setup='from __main__ import call',
        number=COUNT,
    )
    print('Total time %.4f' % result_sec)
    result_usec = result_sec * 1000000
    result_per_call = result_usec / COUNT
    print('%.4f usec per call' % result_per_call)

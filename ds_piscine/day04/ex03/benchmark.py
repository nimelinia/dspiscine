#!/usr/local/bin/python3


import timeit
import sys
from functools import reduce


def reduce_(num):
    result = reduce(lambda x, y: x + y**2, range(num))
    return result


def cycle(num):
    result = 0
    for i in range(num):
        result += i ** 2
    return result


def counting():
    if len(sys.argv) != 4:
        raise BaseException
    num = int(sys.argv[3])
    count_of_it = sys.argv[2]
    d = {'loop': f'cycle({num})', 'reduce': f'reduce({num})'}
    if sys.argv[1] not in d.keys():
        raise BaseException
    func = d[sys.argv[1]]
    time_ = timeit.timeit(lambda: func, count_of_it)
    print(time_)


if __name__ == '__main__':
    try:
        counting()
    except:
        print('Something wrong')
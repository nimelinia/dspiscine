#!/usr/local/bin/python3


import timeit
import random
from collections import Counter as cnt


def generating():
    result = [random.randint(0, 100) for _ in range(1000000)]
    return result


def create_dict(lst):
    d = dict()
    for i in range(101):
        d[i] = lst.count(i)
    return d


def find_top10(lst):
    d = create_dict(lst)
    my_d = dict()
    for (num, countnum) in sorted(d.items(), key=lambda item: (-int(item[1]), item[0]))[:10]:
        my_d[num] = countnum
    return my_d


def create_dict_cnt(lst):
    return (dict(cnt(lst)))


def find_top10_cnt(lst):
    return(dict(cnt(lst).most_common(10)))


def counting():
    lst = generating()
    print('my function: ' + str(timeit.Timer(lambda: create_dict(lst)).timeit(1)))
    print('Counter: ' + str(timeit.Timer(lambda: create_dict_cnt(lst)).timeit(1)))
    print('my top: ' + str(timeit.Timer(lambda: find_top10(lst)).timeit(1)))
    print('Counter\'s top: ' + str(timeit.Timer(lambda: find_top10_cnt(lst)).timeit(1)))


if __name__ == '__main__':
    try:
        counting()
    except:
        print('Something wrong')
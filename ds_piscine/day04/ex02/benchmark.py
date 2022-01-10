#!/usr/local/bin/python3


import timeit
import sys


def get_emails():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    return emails


def cycle():
    buf = get_emails()
    result = []
    for mail in buf:
        result.append(mail)
    return result


def list_comprehension():
    buf = get_emails()
    result = [mail for mail in buf]
    return result


def use_map():
    buf = get_emails()
    result = list(map(lambda x: x, buf))
    return result


def use_filter():
    buf = get_emails()
    result = list(filter(lambda x: x, buf))
    return result


def counting():
    if len(sys.argv) != 3:
        raise BaseException
    count_of_it = sys.argv[2]
    d = {'loop': 'cycle()', 'list_comprehension': 'list_comprehension()', 'map': 'use_map()', 'filter': 'use_filter()'}
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
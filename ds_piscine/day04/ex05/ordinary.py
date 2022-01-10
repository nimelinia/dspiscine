#!/usr/local/bin/python3

import sys
import resource


def create_list():
    if len(sys.argv) != 2:
        raise Exception
    path = sys.argv[1]
    lst = []
    with open(path, 'r') as file:
        for line in file:
            lst.append(line)
    return lst


if __name__ == '__main__':
    try:
        lst = create_list()
        for i in lst:
            pass
        res = resource.getrusage(resource.RUSAGE_SELF)
        print('Peak Memory Usage = ' + format(res.ru_maxrss / (1024**3), '0.3f') + ' GB')
        print('User Mode Time + System Mode Time = ' + format(res.ru_utime + res.ru_stime, '0.2f') + 's')
    except:
        print('Something wrong')
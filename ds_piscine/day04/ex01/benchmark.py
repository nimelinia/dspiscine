#!/usr/local/bin/python3


import timeit


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


def comparing():
    count_of_it = 90000000
    time_1 = timeit.Timer(lambda: cycle()).timeit(count_of_it)
    time_2 = timeit.Timer(lambda: list_comprehension()).timeit(count_of_it)
    time_3 = timeit.Timer(lambda :use_map()).timeit(count_of_it)
    times = sorted([time_1, time_2, time_3])
    if times[0] == time_2:
        print('it is better to use a list comprehension')
    elif times[0] == time_1:
        print('it is better to use a loop')
    else:
        print('it is better to use a map')
    print(str(times[0]) + ' vs ' + str(times[1]) + ' vs ' + str(times[2]))


if __name__ == '__main__':
    comparing()
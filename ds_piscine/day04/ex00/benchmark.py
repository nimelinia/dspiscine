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


def comparing():
    count_of_it = 90000000
    time_1 = timeit.Timer(lambda: cycle()).timeit(count_of_it)
    time_2 = timeit.Timer(lambda: list_comprehension()).timeit(count_of_it)
    if time_1 >= time_2:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(str(min(time_2, time_1)) + ' vs ' + str(max(time_2, time_1)))


if __name__ == '__main__':
    comparing()
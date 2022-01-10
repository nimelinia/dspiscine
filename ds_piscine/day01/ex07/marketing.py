import sys


def set_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
               'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return to_set(clients)


def set_partic():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return to_set(participants)


def set_recip():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return to_set(recipients)


def call_center():
    return set_clients().difference(set_recip())


def pot_clients():
    return set_partic() - set_clients()


def loy_pro():
    return set_clients() - set_partic()


def choose_func(name):
    if name == 'call_center':
        return to_list(call_center())
    if name == 'potential_clients':
        return to_list(pot_clients())
    if name == 'loyalty_program':
        return to_list(loy_pro())


def check_name(name):
    if name == 'call_center' or name == 'potential_clients' or name == 'loyalty_program':
        return True
    return False


def to_set(list_):
    # print(set(list_))
    return set(list_)


def to_list(set_):
    print(list(set_))
    return list(set_)


def main():
    if len(sys.argv) != 2:
        return
    if check_name(sys.argv[1]) is False:
        raise ValueError
    return choose_func(sys.argv[1])


if __name__ == '__main__':
    main()
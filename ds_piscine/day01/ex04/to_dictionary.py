def list_of_tuples():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples


def print_dict(d):
    for key in d.keys():
        for val in d[key]:
            print("'" + str(key) + "'", end=' : ')
            print("'" + val + "'")


def to_dictionary():
    d = dict()
    lst = list_of_tuples()
    for tpl in lst:
        if tpl[1] not in d:
            d[tpl[1]] = [tpl[0]]
        else:
            d[tpl[1]].append(tpl[0])
    print_dict(d)


if __name__ == '__main__':
    to_dictionary()
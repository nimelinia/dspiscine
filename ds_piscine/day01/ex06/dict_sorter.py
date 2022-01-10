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


def sort_dict():
    d = dict()
    lst = list_of_tuples()
    for tpl in lst:
        d[tpl[0]] = tpl[1]
    for (country, _) in sorted(d.items(), key=lambda item: (-int(item[1]), item[0])):
        print(country)


if __name__ == '__main__':
    sort_dict()
def change_line(line):
    ret = line
    for num, i in enumerate(line):
        if i == ',' and num < len(line) - 1 and line[num + 1] != ' ':
            ret = ret[:num] + line[num:].replace(',', '\t', 1)
    return ret


def ad_line(line, new_file):
    new_file.write(change_line(line))


def read_file():
    with open('ds.tsv', 'a') as new_file:
        with open('ds.csv', 'r') as file:
            for line in file:
                ad_line(line, new_file)


if __name__ == '__main__':
    read_file()
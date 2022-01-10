import sys


def parse(line, file):
    name_surname = line.split('@')[0].split('.')
    file.write(name_surname[0].capitalize() + '\t' + name_surname[1].capitalize() + '\t' + line + '\n')


def main():
    if len(sys.argv) != 2:
        return
    with open('employees.tsv', 'a') as emp_f:
        emp_f.write('Name\tSurname\tE-mail\n')
        with open(sys.argv[1], 'r') as file:
            for line in file:
                parse(line.strip(), emp_f)


if __name__ == '__main__':
    main()
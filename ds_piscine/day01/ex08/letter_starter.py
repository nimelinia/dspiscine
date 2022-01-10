import sys


def parse(line, file):
    name_surname = line.split('@')[0].split('.')
    file.write(name_surname[0].capitalize() + '\t' + name_surname[1].capitalize() + '\t' + line + '\n')


def main():
    if len(sys.argv) != 2:
        return
    datas = []
    with open('employees.tsv', 'r') as emp_f:
        for line in emp_f:
            if sys.argv[1] in line:
                datas = line.split('\t')
                break
    if len(datas):
        # print(f'Dear {datas[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. ' \
        #        f'That’s a precondition for the professionals that our company hires.')
        return f'Dear {datas[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. ' \
               f'That’s a precondition for the professionals that our company hires.'
    return


if __name__ == '__main__':
    main()
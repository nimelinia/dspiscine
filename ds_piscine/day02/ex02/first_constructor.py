import sys
import os


def check_line(line, num):
    if line.count(',') != 1:
        raise Exception('Wrong delimiter')
    if num == 0:
        if type(line.split(',')[0]) != str or type(line.split(',')[1]) != str:
            raise Exception('Wrong text format')
    else:
        if line.split(',')[0].isdigit() is False or line.split(',')[1].strip().isdigit() is False or \
            int(line.split(',')[0]) not in range(0, 2) or int(line.split(',')[1].strip()) not in range(0, 2) or \
                line.split(',')[0] == line.split(',')[1].strip():
            raise Exception('Wrong format of lines')


class Research:
    def __init__(self, path):
        self.file = path

    def file_reader(self):
        ret = ''
        try:
            with open(self.file, 'r') as file:
                num = 0
                for line in file:
                    check_line(line, num)
                    ret += line
                    num += 1
        except FileNotFoundError:
            ret = "There is no file"
        return ret


def main():
    if len(sys.argv) != 2:
        return
    path = sys.argv[1]
    print(Research(path).file_reader())


if __name__ == '__main__':
    main()
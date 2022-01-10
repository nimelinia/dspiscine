import sys
import os


class Research:
    def __init__(self, path):
        self.file = path

    def check_header(self, line):
        if line.count(',') != 1:
            raise Exception('Wrong delimiter')
        if line.split(',')[0].isdigit() or line.split(',')[1].strip().isdigit():
            return False
        return True

    def check_line(self, line):
        if line.count(',') != 1:
            raise Exception('Wrong delimiter')
        if line.split(',')[0].isdigit() is False or line.split(',')[1].strip().isdigit() is False or \
                int(line.split(',')[0]) not in range(0, 2) or int(line.split(',')[1].strip()) not in range(0, 2) or \
                line.split(',')[0] == line.split(',')[1].strip():
            raise Exception('Wrong format of lines')

    def file_reader(self):
        ret = []
        has_header = True
        try:
            with open(self.file, 'r') as file:
                for num, line in enumerate(file):
                    if num == 0:
                        has_header = self.check_header(line)
                        if has_header:
                            continue
                    self.check_line(line)
                    ret.append([int(line.split(',')[0]), int(line.split(',')[1].strip())])
        except FileNotFoundError:
            ret = ['There is no file']
        return ret

    class Calculations:
        def counts(self, datas):
            heads = 0
            tails = 0
            for i in datas:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        def fractions(self, heads, tails):
            return heads / (heads + tails), tails / (heads + tails)

def main():
    if len(sys.argv) != 2:
        return
    path = sys.argv[1]
    datas = Research(path).file_reader()
    print(datas)
    if datas == ['There is no file']:
        return
    heads, tails = Research.Calculations.counts(Research.Calculations(), datas)
    print(heads, end=' ')
    print(tails)
    per_head, per_tail = Research.Calculations.fractions(Research.Calculations(), heads, tails)
    print(per_head, end=' ')
    print(per_tail)


if __name__ == '__main__':
    main()
import sys
from random import randint


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
        def __init__(self, datas):
            self.datas = datas
            self.heads = 0
            self.tails = 0

        def counts(self):
            heads = 0
            tails = 0
            for i in self.datas:
                if i[0] == 1:
                    heads += 1
                else:
                    tails += 1
            self.heads = heads
            self.tails = tails
            return heads, tails

        def fractions(self):
            if (self.heads + self.tails) == 0:
                return
            return self.heads / (self.heads + self.tails), self.tails / (self.heads + self.tails)


class Analytics(Research.Calculations):
    def predict_random(self, num):
        ret = []
        for i in range(num):
            a = randint(0, 1)
            ret.append([a, (a + 1) % 2])
        return ret

    def predict_last(self):
        return self.datas


def main():
    if len(sys.argv) != 2:
        return
    path = sys.argv[1]
    datas = Research(path).file_reader()
    calculations = Research.Calculations(datas)
    if datas == ['There is no file']:
        print(datas)
        return
    print('\33[1m\33[35mResult of file_reader:    \33[34m', end='')
    print(datas)
    print('\33[35mResult of count:          \33[34m', end='')
    print(calculations.counts())
    print('\33[35mResult of fraction:       \33[34m', end='')
    print(calculations.fractions())
    print('\33[35mResult of predict_random: \33[34m', end='')
    print(Analytics.predict_random(Analytics(datas), 8))
    print('\33[35mResult of predict_last:   \33[34m', end='')
    print(Analytics.predict_last(Analytics(datas)), end='')
    print('\33[0m')

import sys


class WrongNumberOfArguments(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Wrong number of arguments, {self.message}'
        else:
            return f'Wrong number of arguments'


class WrongSymbols(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Wrong symbols, {self.message}'
        else:
            return f'Wrong symbols'


def decode_str(str_, shift, alpha):
    ret = ''
    for sym in str_:
        if sym in alpha:
            ret += alpha[(alpha.index(sym) - shift) % 26]
        else:
            ret += sym
    print(ret)


def encode_str(str_, shift, alpha):
    ret = ''
    for sym in str_:
        if sym in alpha:
            ret += alpha[(alpha.index(sym) + shift) % 26]
        else:
            ret += sym
    print(ret)


def main():
    if len(sys.argv) != 4:
        raise WrongNumberOfArguments
    command_ = sys.argv[1]
    str_ = sys.argv[2]
    shift = int(sys.argv[3])
    if str_.isascii() == False:
        raise WrongSymbols
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if command_ == 'decode':
        decode_str(str_, shift, alpha)
    elif command_ == 'encode':
        encode_str(str_, shift, alpha)
    else:
        print('Wrong command')


if __name__ == '__main__':
    main()
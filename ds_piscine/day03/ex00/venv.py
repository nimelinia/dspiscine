import os
import termgraph

def print_the_name():
    try:
        print('Your current virtual env is ' + str(os.environ['VIRTUAL_ENV']))
    except KeyError:
        print('Your venv was deactivated')


if __name__ == '__main__':
    print_the_name()


    # deactivate - чтобы деактивировать venv
    # python3 -m venv path/scopycat - чтобы создать
    # source path/scopycat/bin/activate - чтобы активировать
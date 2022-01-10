class Research:
    def file_reader(self):
        file = 'data.csv'
        ret = ''
        try:
            with open(file, 'r') as file:
                for line in file:
                    ret += line
        except FileNotFoundError:
            print("There is no file")
        return ret

def main():
    print(Research().file_reader())


if __name__ == '__main__':
    main()
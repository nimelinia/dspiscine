class Must_read:
    file = 'data.csv'
    try:
        with open(file, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("There is no file")


def main():
    Must_read()


if __name__ == '__main__':
    main()
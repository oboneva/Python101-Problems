import sys


def cat(arguments):
    with open(arguments, 'r') as file:
        for line in file:
            print(line, end="")


def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()

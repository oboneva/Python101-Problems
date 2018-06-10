import sys


def sum_numbers(filename):
    with open(filename) as file:
        return sum([int(i) for i in file.read().split()])


def main():
    print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
    main()

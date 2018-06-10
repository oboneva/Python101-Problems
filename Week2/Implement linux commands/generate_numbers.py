import sys
from random import randint


def generate_numbers(filename, numbers):
    random_numbers = [str(randint(1, 1000)) for i in range(int(numbers))]

    with open(filename, 'w') as file:
        file.write(" ".join(random_numbers))


def main():
    generate_numbers(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()

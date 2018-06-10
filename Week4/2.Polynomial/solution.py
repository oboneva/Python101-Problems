import sys
from polynomial import Polynomial


def main():
    polynomial = Polynomial.parse_from_string(sys.argv[1])
    print("The derivative of f(x) = {} is:".format(str(polynomial)))
    print("f'(x) = {}".format(polynomial.differentiation()))


if __name__ == '__main__':
    main()

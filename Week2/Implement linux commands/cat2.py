import sys
from cat import cat as cat_func


def cat2(arguments):
    for i in arguments[1:]:
        cat_func(i)


def main():
    cat2(sys.argv)

if __name__ == '__main__':
    main()

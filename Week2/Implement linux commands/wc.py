import sys


def count_chars(filename):
    with open(filename) as f:
        return f.seek(0, 2)


def count_words(filename):
    with open(filename) as f:
        content = f.read()
        words = content.split()
        return len(words)


def count_lines(filename):
    with open(filename) as f:
        content = f.read()
        lines = content.split('\n')
        return len(lines)


def count(argument, filename):
    if(argument == 'chars'):
        return count_chars(filename)
    elif (argument == 'words'):
        return count_words(filename)
    elif (argument == 'lines'):
        return count_lines(filename)


def main():
    print(count(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()

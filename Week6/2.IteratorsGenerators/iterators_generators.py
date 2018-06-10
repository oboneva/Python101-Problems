from os import listdir
from os.path import isfile, join
import os
import random
import string


def compress(iterable, mask):
    return [iterable[i] for i in range(len(mask)) if mask[i]]


def get_files(path):
    files = []
    for f in listdir(path):
        if isfile(join(path, f)):
            files.append('{}/{}'.format(path, f))

    return files


def get_next_line(path):
    files = get_files(path)

    for file in sorted(files):
        with open(file, 'r') as f:
            for line in f:
                yield line


def generate_chapter(path):
    chapter = []

    for line in get_next_line(path):
        if line.startswith('#') and len(chapter) > 0:
            yield "".join(chapter)
            chapter = []
        chapter.append(line)

    yield "".join(chapter)


def book_reader():
    path = "{}/Book".format(os.getcwd())
    for chapter in generate_chapter(path):
        user_input = input('Press Enter for next chapter: ')
        if user_input == '':
            print(chapter)


def generate_word():
    length = int(random.random() * 10)

    word_chars = []
    for i in range(length):
        word_chars.append(random.choice(string.ascii_letters))

    return "".join(word_chars)


def generate_chapter(length, chapter_num):
    words = ['# Chapter {}\n'.format(chapter_num)]

    for i in range(length):
        words.append(generate_word())

    return " ".join(words)


def generate_book(chapter_count, chapter_length):
    with open('Book.txt', 'w') as f:
        pass

    for i in range(chapter_count):
        with open('Book.txt', 'a') as f:
            f.write(generate_chapter(chapter_length, i + 1))
            f.write('.\n\n')


if __name__ == '__main__':
    main()

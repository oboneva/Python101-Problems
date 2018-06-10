def sum_of_digits(number):
    return sum([int(i) for i in list(str(abs(number)))])

def to_digits(n):
    return [int(i) for i in list(str(abs(n)))]

def to_number(digits):
    digits_list = [str(i) for i in digits]

    return int(''.join(digits_list))

def fact(n):
    if n <= 1:
        return 1

    return n * fact(n - 1)

def fact_digits(n):
    digits = to_digits(n)

    return sum([fact(i) for i in digits])

def fibonacci(n):
    result = []
    a, b = 0, 1

    while len(result) < n:
        result.append(b)
        a, b = b, a + b

    return result

def fib_number(number):
    numbers = fibonacci(number)

    return to_number(numbers)

def palindrome(n):
    if type(n) is int:
        n = str(n)

    reversed_n = n[::-1]

    return reversed_n == n

def count_vowels(string):
    return sum([i.lower() in 'aeiouy' for i in string])

def count_consonants(string):
    return sum([i.lower() in 'bcdfghjklmnpqrstvwxz' for i in string])

def char_histogram(string):
    histogram = {}
    for i in string:

        if i in histogram:

            histogram[i] += 1
        else:
            histogram[i] = 1

    return histogram

def count_substrings(haystack, needle):
    count = 0
    length = len(needle)

    i = 0
    while i < len(haystack) - length + 1:
        if haystack[i: length + i] == needle:
            count += 1
            i += length - 1
        i += 1

    return count

def sum_matrix(m):
    sum = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            sum += m[i][j]

    return sum

def nan_expand(n):
    if n == 0:
        return ''
    if n == 1:
        return 'NaN'

    return 'Not a ' + nan_expand(n - 1)

def generate_primes(n):
    numbers = [True] * n
    primes = []

    for i in range(2, n):
        if numbers[i]:
            primes.append(i)
            for j in range(i**2, n, i):
                numbers[j] = False

    return primes

def prime_factorization(n):
    primes = generate_primes(n + 1)

    if n in primes:
        return [(n, 1)]

    result = []

    power = 0
    for x in primes:
        while n % x == 0:
            n /= x
            power += 1
        if power > 0:
            result.append((x, power))
            power = 0
            for y in primes:
                while n % y == 0:
                    n /= y
                    power += 1
                if power > 0:
                    result.append((y, power))
                    return result

def group1(lst):
    res = []
    list_1 = []

    for i in range(len(lst)):
        if i == 0:
            list_1.append(lst[i])
        else:
            if lst[i] == lst[i-1]:
                list_1.append(lst[i])
            else:
                res.append(list_1)
                list_1 = [lst[i]]
    res.append(list_1)

    return res

def max_consecutive(items):
    return max([len(x) for x in group1(items)])

def is_valid(i, j, rows, cols):
    return i >= 0 and i < rows and j >= 0 and j < cols

def word_in_specific_direction(matrix, coord_row, coord_column, rows, cols, direction, word_len):
    word = matrix[coord_row][coord_column]
    new_x, new_y = coord_row, coord_column

    for i in range(word_len):
        new_x, new_y = new_x + direction[0], new_y + direction[1]
        if is_valid(new_x, new_y, rows, cols):
            word += matrix[new_x][new_y]
        else:
            return ""

    return word

def matched_words(matrix, coord_x, coord_y, rows, cols, word):
    count = 0
    row_and_cols = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for direction in row_and_cols:
        if word == word_in_specific_direction(matrix, coord_x, coord_y, rows, cols, direction, len(word) - 1):
            count += 1

    return count

def is_palindrome(string):
    return string == string[::-1]

def word_count():
    word = input()
    rows, cols = input().split()
    rows, cols = int(rows), int(cols)

    if len(word) > int(rows) or len(word) > int(cols):
        return 'Invalid number of rows or columns!'

    matrix = []
    for i in range(int(rows)):
        line = input()
        matrix.append(line.split())

    count = 0

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == word[0]:
                count += matched_words(matrix, x, y, rows, cols, word)

    if is_palindrome(word):
        count /= 2

    return count

def gas_station(distance, tank_size, stations):
    stations.insert(0, 0)
    stations.append(distance)
    fuel = tank_size
    result = []
    for i in range(len(stations) - 1):
        dist_to_next = stations[i + 1] - stations[i]
        if(fuel < dist_to_next):
            result.append(stations[i])
            fuel = tank_size

        fuel -= dist_to_next

    return result

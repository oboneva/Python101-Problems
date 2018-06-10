def is_number_balanced(number):
    list_of_digits = list(str(number))
    middle = len(list_of_digits) // 2

    if middle == 0:
        return True

    left_part = 0
    right_part = 0

    for i in range(middle):
        left_part += int(list_of_digits[i])
        right_part += int(list_of_digits[-i - 1])

    return left_part == right_part

def increasing_or_decreasing(sequence):
    down = False
    if(sequence[0] > sequence[1]):
        sequence = sequence[::-1]
        down = True

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False

    if down:
        return 'Down!'
    else:
        return 'Up!'

def get_largest_palindrome(number):
    list_of_digits = ([int(i) for i in list(str(number))])
    result = []

    i = 0
    for i in range(len(list_of_digits) // 2):
        result.insert(i, list_of_digits[i])
        result.insert(-i - 1, list_of_digits[i])

    if len(list_of_digits) % 2 == 1:
        result.insert(i + 1, list_of_digits[i + 1])

    result_number = int("".join([str(i) for i in result]))

    if len(result) % 2 == 1 and result_number >= number:
        result[i + 1] -= 1
        return int("".join([str(i) for i in result]))

    while result_number >= number:
        result[len(result) // 2 - 1] -= 1
        result[len(result) // 2] -= 1
        result_number = int("".join([str(i) for i in result]))

    return int("".join([str(i) for i in result]))

def sum_of_numbers(input_string):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    list_of_chars = list(input_string)
    number = ''
    sum2 = 0

    for i in list_of_chars:
        if i in digits:
            number += i
        else:
            if number != '':
                sum2 += int(number)
                number = ''
    if(number != ''):
        sum2 += int(number)

    return sum2

def birthday_ranges(birthdays, ranges):
    result = []

    for x, y in ranges:
        result.append(sum([i >= x and i <= y for i in birthdays]))

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

def numbers_to_message(pressed_sequence):
    list_of_groups = group1(pressed_sequence)
    SPACE = ' '
    FIRST_BUTTON_DIGIT = 2

    message = ''
    buttons = [('a', 3), ('d', 3), ('g', 3), ('j', 3),
               ('m', 3), ('p', 4), ('t', 3), ('w', 4)]
    capital_letter = False

    for group in list_of_groups:
        letter = ''
        digit = group[0]
        if digit == 0:
            letter = SPACE
        elif digit == -1:
            continue
        elif capital_letter:
            letter = chr(ord(buttons[digit - FIRST_BUTTON_DIGIT][0]) +
                    (len(group) - 1) % buttons[digit - FIRST_BUTTON_DIGIT][1])
            letter = letter.capitalize()
            capital_letter = False
        elif digit == 1:
            capital_letter = True
        else:
            letter = chr(ord(buttons[digit - FIRST_BUTTON_DIGIT][0]) +
                    (len(group) - 1) % buttons[digit - FIRST_BUTTON_DIGIT][1])
        message += letter

    return message

def message_to_numbers(message):
    buttons = {'a': 2, 'd': 3, 'g': 4, 'j': 5, 'm': 6, 'p': 7, 't': 8, 'w': 9}
    SPACE = ' '

    pressed_sequence = []

    for char in message:
        if char == SPACE:
            pressed_sequence.append(0)
            continue
        elif char.isupper():
            char = char.lower()
            pressed_sequence.append(1)

        repetition_count = 1
        while chr(ord(char)) not in buttons.keys():
            repetition_count += 1
            char = chr(ord(char) - 1)

        if len(pressed_sequence) > 0 and pressed_sequence[-1] == buttons[char]:
            pressed_sequence.append(-1)

        pressed_sequence.extend([buttons[char]] * repetition_count)

    return pressed_sequence

def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    people_count = 0
    people_count_prev = 0
    weight = 0
    trips = 0

    for x in people_weight:
        if weight + x <= max_weight and people_count < max_people:
            weight += x
            people_count += 1
        else:
            trips += len(set(people_floors[people_count_prev:
                                           people_count + people_count_prev])) + 1
            people_count_prev, people_count, weight = people_count, 0, 0

    if len(set(people_floors[people_count_prev:])) > 0:
        trips += len(set(people_floors[people_count_prev:])) + 1

    return trips

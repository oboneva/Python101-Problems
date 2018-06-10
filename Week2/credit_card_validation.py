def is_credit_card_valid(number):
    number_list = list(str(number))

    if len(number_list) % 2 == 0:
        return False

    even_digits = [int(i) for i in number_list[::2]]
    odd_digits = list(''.join([str(int(i) * 2) for i in number_list[1::2]]))
    odd_digits = [int(i) for i in odd_digits]

    if (sum(even_digits) + sum(odd_digits)) % 10 == 0:
        return "Valid!"
    else:
        return "Invalid!"

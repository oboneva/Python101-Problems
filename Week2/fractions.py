from math import gcd


def simplify_fraction(fraction):
    assert type(fraction) is tuple
    assert fraction[1] is not 0

    return (fraction[0] // gcd(fraction[0], fraction[1]), fraction[1] // gcd(fraction[0], fraction[1]))


def collect_fractions(fractions):
    assert type(fractions[0]) is tuple
    assert type(fractions[1]) is tuple
    assert type(fractions) is list

    assert fractions[0][1] is not 0
    assert fractions[0][1] is not 0

    nominator = (fractions[0][0] * fractions[1][1] +
                 fractions[0][1] * fractions[1][0])
    denominator = fractions[0][1] * fractions[1][1]

    new_fraction = (nominator, denominator)

    return simplify_fraction(new_fraction)


def sort_fractions(fractions):
    assert type(fractions) is list

    decimal_fraction_dict = {x[0] / x[1]: x for x in fractions}
    decimals = [x[0] / x[1] for x in fractions]
    decimals.sort()

    fractions_sorted = [decimal_fraction_dict[x] for x in decimals]

    return fractions_sorted

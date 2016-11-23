from math import log10


def how_many_digits(number):
    return int(log10(number))


def reverse_num(value):
    if not isinstance(value, int):
        raise ValueError(
            'Unexpected value for reverse_num which requires integers. '
            'Passed type = %s', type(value))
    if -10 < value < 10:
        return value

    last_digit = value % 10
    rest = value // 10
    return last_digit * 10 ** how_many_digits(value) + reverse_num(rest)

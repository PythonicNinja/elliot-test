
def reverse_num(value):
    if not isinstance(value, int):
        raise ValueError(
            'Unexpected value for reverse_num which requires integers. '
            'Passed type = %s', type(value))
    if -10 < value < 10:
        return value

    result = None
    while value != 0:
        last_digit = value % 10

        if result is None:
            result = last_digit
        else:
            result = result * 10 + last_digit

        value //= 10

    return result

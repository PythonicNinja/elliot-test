
def reverse_num(value):
    if not isinstance(value, int):
        raise ValueError(
            'Unexpected value for reverse_num which requires integers. '
            'Passed type = %s', type(value))
    return int(str(value)[::-1])

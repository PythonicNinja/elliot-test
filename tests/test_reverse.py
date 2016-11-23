import pytest

from utils.reverse import reverse_num


@pytest.mark.parametrize('value,expected_result', [
    (130, 31),
    (123, 321),
    (-9, -9),
    (9, 9),
])
def test_reverse_num(value, expected_result):
    assert reverse_num(value) == expected_result


@pytest.mark.parametrize('value', [
    'string',
])
def test_unexpected_type(value):
    with pytest.raises(ValueError):
        reverse_num(value)

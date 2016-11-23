import pytest

from utils.reverse import reverse_num


@pytest.mark.parametrize('value,expected_result', [
    (130, 31),
])
def test_reverse_num(value, expected_result):
    assert reverse_num(value) == expected_result

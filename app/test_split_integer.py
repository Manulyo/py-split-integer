from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(35, 5)
    assert sum(result) == 35


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = split_integer(15, 5)
    assert result == [3, 3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(5, 1)
    assert result == [5]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(21, 7)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(2, 4)
    assert result == sorted(result)
    assert sum(result) == 2
    assert len(result) == 4

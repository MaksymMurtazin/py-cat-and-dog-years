import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [15, 15]),
        (2, 2, [24, 24]),
        (3, 3, [28, 29]),
        (4, 4, [32, 34]),
        (5, 6, [36, 44]),
        (1500, 1500, [6016, 7514])
    ]
)
def test_all_functionality_have_to_work_correctly(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        (-1, -10, TypeError),
        ("10", "1", TypeError),
        ([3], {4}, TypeError),
        ((1,), {2: 3}, TypeError),
    ]
)
def test_raise_error_if_type_of_input_data_is_incorrect(
        cat_age: int,
        dog_age: int,
        expected_error: type[TypeError]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

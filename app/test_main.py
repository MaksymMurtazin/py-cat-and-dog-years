import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, -5, [0, 0]),
        (-1, -10, [0, 0]),
        (1, 1, [15, 15]),
        (2, 2, [24, 24]),
        (3, 3, [28, 29]),
        (4, 4, [32, 34]),
        (5, 6, [36, 44]),
        (1500, 1500, [6016, 7514]),
    ]
)
def test_all_functionality_have_to_work_correctly(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected

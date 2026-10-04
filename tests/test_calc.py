from src.calc import add, divide, running_total


def test_add():
    assert add(2, 2) == 4


def test_divide():
    assert divide(10, 2) == 5


def test_running_total():
    assert running_total([1, 2, 3]) == [1, 3, 6]

from src.discount import apply_discount


def test_ten_percent_off():
    assert apply_discount(200, 10) <= 200


def test_never_below_zero():
    assert apply_discount(50, 150) == 0


def test_no_discount():
    assert apply_discount(80, 0) == 80

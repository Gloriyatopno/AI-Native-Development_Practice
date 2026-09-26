from copilot_refactoring import calculate_total_price


def test_calculate_total_price_normal_calculation():
    assert calculate_total_price(100, 2, 10) == 180.0


def test_calculate_total_price_zero_discount():
    assert calculate_total_price(75, 3, 0) == 225.0


def test_calculate_total_price_zero_quantity():
    assert calculate_total_price(100, 0, 20) == 0.0


def test_calculate_total_price_higher_discount():
    assert calculate_total_price(200, 2, 75) == 100.0
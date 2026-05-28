def celsius_to_fahrenheit(celsius):
    return round(((celsius * 1.8) + 32), 2)


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0


def test_body_temperature():
    assert celsius_to_fahrenheit(37) == 98.6


def test_negative_celsius():
    assert celsius_to_fahrenheit(-40) == -40.0


def test_rounding():
    assert celsius_to_fahrenheit(37.5) == 99.5

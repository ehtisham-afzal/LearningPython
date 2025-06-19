from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# run the tests of this file with command "pytest test_calculator_with_pytest.py"
# learn more aboute pytest at thier docs on https://docs.pytest.org

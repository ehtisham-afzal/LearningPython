from calculator import square


def main():
    test_square()


# testing with assert and exceptions
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("the square of 2 is not equals to 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("the square of 3 is not equals to 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("the square of -2 is not equals to 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("the square of -3 is not equals to 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("the square of 0 is not equals to 0")


# testing with assert
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9


# tesing manualy
# def test_square():
#     if square(2) != 4:
#         print("the square of 2 is not equals to 4")
#     if square(3) != 9:
#         print("the square of 3 is not equals to 9")


if __name__ == "__main__":
    main()

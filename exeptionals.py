def main():
    x = get_number("what's x ")
    print("x is ", x)


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()

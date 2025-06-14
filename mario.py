def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(blocks):
    # first method
    for _ in range(blocks):
        print("#", end="")
    print()

    # second method
    # print("#" * blocks)


main()

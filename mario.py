def main():
    height = int(input("Height: "))
    print_pyramid(height)


def print_pyramid(height):
    for row in range(height):
        print("❎" * (row + 1))


main()

























# def square():
#     height = int(input("Height: "))
#     print_square(height)


# def print_square(size):
#     for _ in range(size):
#         print_row(size)


# def print_row(blocks):
#     # first method
#     for _ in range(blocks):
#         print("❎", end="")
#     print()

#     # second method
#     # print("❎" * blocks)


# square()

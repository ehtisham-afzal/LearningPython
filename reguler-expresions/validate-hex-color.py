import re


def main():
    color = input("type a hex color code here ")

    pattern = r"^#[0-9A-Fa-f]{6}$"

    match = re.search(pattern, color)

    if match:
        print("the valid input is", match.group())
    else:
        print("not valid input")


main()

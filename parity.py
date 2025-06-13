def main():
    x = int(input("give me the number so i can say is it Even or Odd "))
    if simpler_is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def simple_is_even(n):
    return True if n % 2 == 0 else False


def simpler_is_even(n):
    return n % 2 == 0


main()

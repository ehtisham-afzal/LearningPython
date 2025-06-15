def while_1():
    i = 3
    while i != 0:
        print("meo")
        i -= 1


def while_2():
    i = 0
    while i < 3:
        print("meo")
        i += 1


def for_loop_1():
    for n in [0, 1, 2]:
        print("meo")


def for_loop_2():
    for _ in [0, 1, 2]:
        print("meo")


def for_loop_3():
    for _ in range(3):
        print("meo")


def loop_print_trick():
    print("meo \n" * 3, end="")


def for_loop_with_input():
    while True:
        n = int(input("What is the value of n? "))
        if n < 0:
            continue
        else:
            break
    for _ in range(n):
        print("meo")


def for_loop_with_input_better():
    while True:
        n = int(input("What is the value of n? "))
        if n > 0:
            break

    for _ in range(n):
        print("meo")


def say_mew_functions():
    number = get_number()
    say_mew(number)


# Say_mew_function Side effects
def get_number():
    while True:
        n = int(input("what is the value of n? "))
        if n > 0:
            return n


def say_mew(times):
    for _ in range(times):
        print("mew")


# while_1()
# while_2()
# for_loop_1()
# for_loop_2()
# for_loop_3()
# loop_print_trick()
# for_loop_with_input()
# for_loop_with_input_better()
say_mew_functions()

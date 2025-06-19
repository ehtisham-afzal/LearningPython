def main():
    name = input("what's your name ")
    print(say_hello(name))


def say_hello(to="world"):
    return f"hello {to}"


if __name__ == "__main__":
    main()

def main():
    """
    unpacking list example using " * "
    """

    coins = [10, 23, 50]
    # unpacking with *
    print(account(*coins))


def account(gold, silver, steel):
    return f"you have {gold} gold coins {silver} silver coins and {steel} steel coins"


if __name__ == "__main__":
    main()

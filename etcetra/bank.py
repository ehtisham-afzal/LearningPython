class Account:
    def __init__(self, initial_balace=0):
        self._balance = initial_balace

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


def main():
    account = Account()
    account.deposit(200)
    account.withdraw(100)
    print("your current balance:",account.balance)


# balance = 0


# def main():
#     print("your balance is", balance)
#     deposit(200)
#     withdraw(100)
#     print("your balance is", balance)


# def deposit(n):
#     global balance
#     balance += n


# def withdraw(n):
#     global balance
#     balance -= n


if __name__ == "__main__":
    main()

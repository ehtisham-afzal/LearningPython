# if else mehtods
def ifElseMethod():
    x = int(input("what is the value of x "))
    y = int(input("what is the value of y "))

    if x < y:
        print("x is less than y")
    elif x > y:
        print("y is greater than x")
    else:
        print("x and y is equals to each other")


# the or method
def orMethod():
    x = int(input("what is the value of x "))
    y = int(input("what is the value of y "))

    if x > y or x < y:
        print("x is not equals to y")
    else:
        print("x is equals to y")


def simpler_or_method():
    x = int(input("what is the value of x "))
    y = int(input("what is the value of y "))
    if x == y:
        print("x is equals to y")
    else:
        print("x is not equals to y")


# Grade with AND method
def Grade():
    Score = int(input("Score: "))
    if Score >= 90 and Score <= 100:
        print("Grade A")
    elif Score >= 80 and Score < 90:
        print("Grade B")
    elif Score >= 70 and Score < 80:
        print("Grade C")
    elif Score >= 60 and Score < 70:
        print("Grade D")
    else:
        print("Grade F")


def simple_Grade_Method():
    Score = int(input("Score: "))

    if 90 <= Score <= 100:
        print("Grade A")
    elif 80 <= Score < 90:
        print("Grade B")
    elif 70 <= Score < 80:
        print("Grade C")
    elif 60 <= Score < 70:
        print("Grade D")
    else:
        print("Grade F")


def simpler_Grade_Method():
    Score = int(input("Score: "))

    if Score >= 90:
        print("Grade A")
    elif Score >= 80:
        print("Grade B")
    elif Score >= 70:
        print("Grade C")
    elif Score >= 60:
        print("Grade D")
    else:
        print("Grade F")


# ifElseMethod()
# orMethod()
# simpler_or_method()
# Grade()
# simple_Grade_Method()
simpler_Grade_Method()

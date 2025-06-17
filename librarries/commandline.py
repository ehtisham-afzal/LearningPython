import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print(f"hello my name is {arg}")

# the result of command commandline.py should be "Too few arguments"
# the result of command commandline.py ehtisham zeesham sanan should be
# hello my name is ehtisham
# hello my name is zeeshan
# hello my name is sanan
# the result of command commandline.py "ehtisham afzal" should be "hello my name is ehtisham afzal"
# the result of command commandline.py ehtisham should be "hello my name is ehtisham"


# second method

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print(f"hello my name is {sys.argv[1]}")

# the result of command commandline.py should be "Too few arguments"
# the result of command commandline.py ehtisham afzal should be "Too many arguments"
# the result of command commandline.py "ehtisham afzal" should be "hello my name is ehtisham afzal"
# the result of command commandline.py ehtisham should be "hello my name is ehtisham"


# the first method

# from sys import argv

# if len(argv) < 2:
#     print("Too few arguments")
# elif len(argv) > 2:
#     print("Too many arguments")
# else:
#     print(f"hello my name is {argv[1]}")

# the result of command commandline.py should be "Too few arguments"
# the result of command commandline.py ehtisham afzal should be "Too many arguments"
# the result of command commandline.py "ehtisham afzal" should be "hello my name is ehtisham afzal"
# the result of command commandline.py ehtisham should be "hello my name is ehtisham"

# learn more about sys.argv at https://docs.python.org/3/library/sys.html

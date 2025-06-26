# print all names on names.txt sorted # minimal method
with open("names.txt") as file:
    # to sort file reverse use revers=True to sorted function like "sorted(file, reverse=True)"
    for name in sorted(file):
        print("hello", name.rstrip())


# print all names on names.txt sorted # basid method

# names = []
# # by defualt the secon argument value of open function is "r" "r means read file"
# with open("names.txt") as file:
#     for name in file:
#         names.append(name.rstrip())

# for name in sorted(names):
#     print("hello", name)


# with open("names.txt", "r") as file:
#     # minimal and right method
#     for line in file:
#         print("hello", line.rstrip())


# one method

#     lines = file.readlines()

# for line in lines:
#     # this will print the names with with two line breaks(\n) one coming from file names and another one is adding from print function at the end
#     # print("hello", line)
#     # solution one remove one line break from print function
#     # print("hello", line, end="")

#     # right and better solution with rstrip() function
#     print("hello", line.rstrip())

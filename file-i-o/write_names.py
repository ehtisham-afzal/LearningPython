name = input("what is your name ")


# now using "with" keyword so we don't have open or close file manually and the code will be much clean and minimal
# open file with name "names.txt" if not exist then create if exist then append the name content into them
with open("names.txt", "a") as file:
    file.write(name + "\n")


# open file with name "names.txt" if not exist then create if exist then append the name content into them
# file = open("names.txt", "a")
# file.write(name + "\n")
# file.close()


# open file with name "names.txt" if not exist then create if exist recreate with name content
# file = open("names.txt", "w")
# file.write(name)
# file.close()

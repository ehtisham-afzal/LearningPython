name = input("What is your name? ").strip().title()
print("Hello ", end="" + name + "!" + "\n")  # Method 1: Using end parameter incorrectly
print("Hello, " + name + "!")  # Method 2: Using string concatenation
print(f"Hello, {name}!")  # Method 3: Using f-string for better readability
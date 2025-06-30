import re


name = input("what's your name? ").strip()
matches = re.match("^(.*), *(.*)$",name)

if matches:
    last, first  = matches.groups()
    name = f"{first} {last}"

print("hello", name)
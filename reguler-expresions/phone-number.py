import re

locations = {"+1": "United states and Canada", "+92": "Pakistan", "+62": "Indonesia"}


def main():
    number = input("type a phone number here ")
    pattern = r"^(?P<country_code>\+\d{1,3})[-| ]\d{3}[-| ]\d{3}[-| ]\d{4}"
    matches = re.search(pattern, number)
    if matches:
        country = matches.group("country_code")
        print("the number is from", locations[country])
    else:
        print("Invalid Phone number")


main()

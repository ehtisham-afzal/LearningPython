def main():
    guests = ["ehtisham", "zeeshan afzal", "sanan khan"]
    for guest in guests:
        print(print_letter(guest, "Princess Peach"))


def print_letter(reciever, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

    Dear {reciever},
    
    you are cordially invited to a ball at
    Peach's castle this evening, 07:00 PM.

    Sencerly {sender}

    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()

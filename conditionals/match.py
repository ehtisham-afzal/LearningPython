name = input("What's your Name? ")

# match name:
#     case "Harry":
#         print("Grafindore")
#     case "Harmione":
#         print("Grafindore")
#     case "Ron":
#         print("Grafindore")
#     case "Draco":
#         print("Slytheren")
#     case _:
#         print("Who ?")

# Simpler match mehtod
match name:
    case "Harry" | "Harmione" | "Ron":
        print("Graffindore")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who ?")

def main():
    history = []

    while True:
        action = input("Action: ")
        match action:
            case "up" | "down" | "left" | "right":
                history.append(action)
                print(history)
            case "undo":
                if len(history) > 0:
                    undon = history.pop()
                    print("Undon action", undon)
                    print(history)
                else:
                    print("no prev commands")
            case "restart":
                history.clear()
            case _:
                print("command not identified")


main()

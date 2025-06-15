WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcom to 'spelling Bee' game")
    print("Your letters is A I P R C H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Gues the word: ")

        # if user guesed super word end the a game early
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You won!")

        # check if the words exist on dictionary then remove that word from dictionary
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! you scored {points} points")

    print("thats the game")


# the dictionary.items() method
def print_words_info(words):
    for word, points in words.items():
        print(f"{word} worth {points} points")


# print_words_info(WORDS)
main()

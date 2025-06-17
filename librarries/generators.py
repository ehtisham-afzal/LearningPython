from random import choice, shuffle
from statistics import mean

# first method

# import random
# coin = random.choice(["heads","tails"])

# second method
# randomly print heads or tails with random.choce() function
coin = choice(["Heads", "Tails"])
print(coin)


cards = ["King", "Queen", "Joker"]
# shuffle the list of cards with random.shuffle() function
shuffle(cards)
for card in cards:
    print(card)

# print the average of 90 to 100 with statistics.mean() function
print("average of 90 to 100", mean([90, 100]))

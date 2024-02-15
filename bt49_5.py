# Selecting a random sample from a list without replacement:

import random

# List of cards
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Select a random sample of 5 cards without replacement
random_sample = random.sample(cards, 5)
print("Random sample of cards:", random_sample)
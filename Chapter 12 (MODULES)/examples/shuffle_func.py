import random

rng = random.Random()

cards = list(range(52)) # Generate ints [0 - 51] representing a pack of cards
                        # converted range object to a full list of 0 to 51 using list() type converter
                        # as shuffle cannot work directly with a lazy promise

print(cards) # initially sorted
rng.shuffle(cards)  # shuffles the pack
print(cards) # shuffled
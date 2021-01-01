import random

rng = random.Random()
number = rng.randrange(1, 100)

guesses = 0
msg = ""

while True:
	guess = int(input(msg + "Guess my number between 1 and 100: "))
	guesses += 1

	if (guess > number):
		msg += str(guess) + "is too high!\n"

	elif (guess < number):
		msg += str(guess) + "is too low!\n"

	else:
		break

input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))
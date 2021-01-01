import random

# Your friend will complete this function

def play_once(human_plays_first):
	"""
	Must play one round of the game. If the parameter
	is True, the human gets to play first, else the
	computer gets to play first. When the round ends,
	the return value of the function is one of
	-1 (human wins), 0 (game drawn), 1 (computer wins).
	"""

	# This is all dummy scaffolding code right at the moment...
	rng = random.Random()
	# Pick a random result between -1 and 1.
	result = rng.randrange(-1,2)
	print("Human plays first={0}, winner={1} ".format(human_plays_first, result))
	return result

human = 0
computer = 0
draws = 0
total_games = 0
human_plays_first = False

#game loop
while (True):

	#computing total games played
	total_games += 1

	#determining who plays first
	if (human_plays_first == True):
		human_plays_first = False
	else:
		human_plays_first = True
	
	#result check, score calculated
	result = play_once(human_plays_first)

	if (result == -1):
		print("Human wins!")
		human += 1

	elif(result == 1):
		print("Computer wins!")
		computer += 1

	else:
		print("Game drawn!")
		draws += 1

	#scores announced
	print("Human score =", human)
	print("Computer score =", computer)
	print("Games drawn =", draws)

	#calculating percentage of human wins
	human_wins_percnt = (human/total_games)*100

	#displaying percentage win:
	print("Percentage of human wins =", human_wins_percnt)

	#what to do next? Play/quit?
	choice = input("Do you want to play again? (yes/no): ")

	if (choice == "no"):	#(total_games == 10000):
		print("Goodbye!")
		break


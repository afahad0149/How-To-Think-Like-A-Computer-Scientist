def play_the_game_once():
	return 0


def regular_end_decision():
	play_the_game_once()
	response = input("Play again? (yes or no): ")

	while (response=="yes"):
		play_the_game_once()
		response = input("Play again? (yes or no): ")

	print("Goodbye!")

def post_test_end_decision():
	while True:
		play_the_game_once()
		response = input("Play again? (yes or no): ")

		if(response != "yes"):
			break

	print("Goodbye!")

regular_end_decision()
post_test_end_decision()


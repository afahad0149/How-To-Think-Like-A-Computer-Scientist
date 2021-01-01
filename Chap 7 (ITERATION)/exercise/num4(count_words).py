#number of words of lenc=gth 5

def count_words(words):
	"""returns the number of words of length 5 present in the input list"""

	count = 0
	for i in words:
		if (len(i) == 5):
			count += 1

	return count

print(count_words([]))
print(count_words(["", "", "", ""]))
print(count_words(["", "", "", "", "     ", ""]))
print(count_words(["for", "", "river", ""]))
print(count_words(["The", "smallest", "ferris", "wheel", "in"
					"the", "world"]))
print(count_words(["Is", "this", "the", "real", "life?"]))
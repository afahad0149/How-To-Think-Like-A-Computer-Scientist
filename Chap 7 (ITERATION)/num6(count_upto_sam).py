#number of words upto an including "sam"

def words_until_sam(words):
	"""returns the number of words upto and including the word "sam"
	in the input list of words"""

	count = 0

	for i in words:
		if (i == "sam"):
			count += 1
			return count
		else:
			count += 1

	return count

print(words_until_sam([]))
print(words_until_sam(["","","","   "]))
print(words_until_sam(["better", "grow", "a", "fucking", "backbone!"]))
print(words_until_sam(["my", "dear", "sam"]))
print(words_until_sam(["samwell", "tarly"]))
print(words_until_sam(["sam", "oh", "sam"]))
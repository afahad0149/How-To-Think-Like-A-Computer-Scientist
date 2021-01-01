def count_a(text):
	"""counts the number of times the letter "a" appears in the string"""
	cnt = 0
	for char in text:
		if (char == "a"):
			cnt += 1
	return cnt

print(count_a("banana"))

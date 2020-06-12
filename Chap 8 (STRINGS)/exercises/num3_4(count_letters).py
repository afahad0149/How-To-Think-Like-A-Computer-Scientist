import string

def count_letters_1 (string, key):
	count = 0
	for char in string:
		if char == key:
			count += 1
	return count	

def count_letters_2 (string, key):
	start = 0
	count = 0
	while (string.find(key, start) != -1):
		count += 1
		start = string.find(key, start) + 1
	return count



fruit = "banana"
print(count_letters_1(fruit, "a"))
print(count_letters_1(fruit, "n"))
print(count_letters_1(fruit, "x"))


print(count_letters_2(fruit, "a"))
print(count_letters_2(fruit, "n"))
print(count_letters_2(fruit, "x"))
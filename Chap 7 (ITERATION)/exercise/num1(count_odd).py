#counting odd numbers

def count_odd(numbers):
	"""Counts the number of odd numbers in a list"""

	count = 0
	for i in numbers:
		if (i%2 == 1):
			count += 1

	return count

print(count_odd([]))
print(count_odd([1,3,5,7,9,11]))
print(count_odd([2,4,6,8,10]))
print(count_odd([1,2,3,4,5,6,7,8,9,10]))
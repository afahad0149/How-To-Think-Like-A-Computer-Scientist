#sum of all negative numbers

def sum_of_negatives(numbers):
	"""returns the sum of all the negative numbers in a list"""

	sum = 0
	for i in numbers:
		if (i<0):
			sum += i
	return sum

print(sum_of_negatives([]))
print(sum_of_negatives([-1, -2, -3, -4, -5, -6, -7, -8, -9]))
print(sum_of_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sum_of_negatives([-2, -4, -6]))
print(sum_of_negatives([-1, -3, -5]))
print(sum_of_negatives([1, 3, 5]))
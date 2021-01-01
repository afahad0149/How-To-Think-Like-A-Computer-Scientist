#sum of all the odd numbers before the first occurence of an even number

def sum_before_even(numbers):
	"""returns the sum of all the odd numbers that occur before the first
	even on the list"""

	sum = 0
	for i in numbers:
		if (i%2 == 0):
			return sum
		else:
			sum += i

	return sum


print(sum_before_even([]))
print(sum_before_even([1, 3, 5, 7, 9, 11]))
print(sum_before_even([2, 4, 6, 8, 10]))
print(sum_before_even([1, 3, 5, 7, 8, 9, 11, 13, 14]))
print(sum_before_even([2, 3, 5, 7, 9, 4, 6]))
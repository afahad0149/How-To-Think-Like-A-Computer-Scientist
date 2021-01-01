#sums of all the even numbers in a list

def sum_of_even(numbers):
	"""Returns the sum of all the even numbers in the input list"""

	sum = 0
	for i in numbers:
		if (i%2 == 0):
			sum += i

	return sum

print(sum_of_even([]))
print(sum_of_even([1,2,3,4,5,6,7,8,9,0,10]))
print(sum_of_even([2,4,6,8]))
print(sum_of_even([1,3,5,7,9]))
#print n triangular numbers

def print_triangular_numbers(n):
	"""prints the first n triangular numbers"""

	for i in range(1, n+1):
		sum = int((i / 2)*(1 + i))
		print(i, "\t", sum)


print_triangular_numbers(5)
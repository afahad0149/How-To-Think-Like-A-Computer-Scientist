def print_multiples (n, high):
	for i in range(1, high+1):
		print(n*i, end="\t")
	print()

def print_multiple_table (high):
	for i in range(1, high+1):
		print_multiples(i, high)

def print_multiple_triangle (high):
	for i in range(1, high+1):
		print_multiples(i, i)


print_multiple_table(9)
print_multiple_triangle(9)
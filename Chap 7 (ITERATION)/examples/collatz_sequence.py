def collatz_seq (n):
	"""prints the 3n+1 sequence halting at n=1"""

	while (n != 1):
		print(n, end = ", ")
		if (n%2 == 0):
			n = n//2
		else:
			n = 3*n + 1

	print (n, end = ".\n")


# collatz_seq(3)
# collatz_seq(19)
# collatz_seq(16)
# collatz_seq(21)
collatz_seq (27) #takes over 100 steps

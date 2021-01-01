#count the number of even digits in a non negative number

import sys

def num_even_digits(n):
	"""counts the number of even digits in a non negative number"""
	if (n == 0):
		return 1

	else:
		count = 0
		while (n!=0):
			dig = n % 10

			if (dig % 2 == 0):
				count += 1

			n //= 10

		return count


def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)


test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)

# print(num_even_digits(-1))
# print(num_even_digits(-1234)) doesnt work for negative numbers

#print(-1234%10, -1234//10) #result = 6, -124
#print(-124%10, -124//10) #result = 6, -13
#print(-13%10, -13//10) #result = 7, -2
#print(-2%10, -2//10) #result = 8, -1
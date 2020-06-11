#find the sum of squares of numbers in a list

import sys

def sum_of_squares(xs):
	"""computes the sum of the squares of each number in a list"""

	total = 0

	for i in xs:
		total += i*i

	return total

def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([ ]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)
test(sum_of_squares([-1, 1, -1 , 1]) == 4)

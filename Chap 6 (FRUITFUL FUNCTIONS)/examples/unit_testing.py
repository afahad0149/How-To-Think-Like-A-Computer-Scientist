import sys

def absolute (num):
	"""Returns the absolute value of num"""

	if (num < 0):
		return -num
	else:
		return num


def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)


def test_suite():
	"""Run the suite of tests for code in this module"""

	test(absolute(17)==17)
	test(absolute(-17)==-17)
	test(absolute(0)==0)
	test(absolute(3.14)==3.14)
	test(absolute(-3.14)==3.14)

test_suite()

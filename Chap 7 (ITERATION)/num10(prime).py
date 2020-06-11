#determines if a number is prime or not

import sys
import math

def is_prime(n):
	"""determines if a number is prime"""

	lim = math.ceil(math.sqrt(n))

	for i in range(2, lim+1):
		if (n % i == 0):
			return False

	return True


def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)


# test(is_prime(11))
# test(not is_prime(35))
# test(is_prime(2017))
# test(is_prime(2011))
# test(is_prime(19911121))
# test(not is_prime(19951020))



#number of days from 19000101 to 19991231 is 36524 (365*100+100/4-1)
#In YYYYMMDD there are 2259 primes.
#So, if we assume that the odds of being born on any given date is about equal (not true)
#and that a given person is a random age between 0 and 100 (also not true)
#print(2259/36524 * 100)
#6.184974263497974 % chance of having a prime birthdate.
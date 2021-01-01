import sys

def find(strng, ch):
	"""
	Find and return the index of ch in strng.
	Return -1 if ch does not occur in strng.
	"""

	ix = 0
	while (ix < len(strng)):
		if (ch == strng [ix]):
			return ix

		ix += 1

	return -1


def find_OP(strng, char, start = 0, end = None):
	"""
	Find and return the index of ch in strng, 
	starting from start upto end.
	Return -1 if ch does not occur in strng.
	"""
	ix = start

	if end is None:
		end = len(strng)

	while (ix < end):
		if (char == strng[ix]):
			return ix
		ix += 1

	return -1


def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)


ss = "Python strings have some interesting methods."
test(find_OP(ss, "s") == 7)
test(find_OP(ss, "s", 7) == 7)
test(find_OP(ss, "s", 8) == 13)
test(find_OP(ss, "s", 8, 13) == -1)
test(find_OP(ss, ".") == len(ss)-1)


#testing built-in find function
test(ss.find("s") == 7)
test(ss.find("s", 7) == 7)
test(ss.find("s", 8) == 13)
test(ss.find("s", 8, 13) == -1)
test(ss.find(".") == len(ss)-1)

#using built-in find to find substrings
print("banana".find("nan"))
print("banana".find("na",3))


test(find("Compsci", "p") == 3)
test(find("Compsci", "C") == 0)
test(find("Compsci", "i") == 6)
test(find("Compsci", "x") == -1)
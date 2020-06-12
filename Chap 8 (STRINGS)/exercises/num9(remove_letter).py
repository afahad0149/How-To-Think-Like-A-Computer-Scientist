import sys

def remove_letter (letter, text):
	result = ""

	for ch in text:
		if ch not in letter:
			result += ch

	return result


def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")
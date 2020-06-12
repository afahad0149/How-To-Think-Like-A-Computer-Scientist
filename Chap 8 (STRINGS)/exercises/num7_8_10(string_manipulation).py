import sys

def reverse (text):
	rev_text = ""
	for i in range(-1, -len(text)-1, -1):
		rev_text += text[i]

	return rev_text

def mirror (text):
	return text + reverse(text)

def is_palindrome (text):
	return text == reverse(text)

def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

# print (reverse("happy"))
# print (reverse("Python"))
# print (reverse(""))
# print (reverse("a"))

# print (mirror("good"))
# print (mirror("Python"))
# print (mirror(""))
# print (mirror("a"))

# test(is_palindrome("abba"))
# test(not is_palindrome("abab"))
# test(is_palindrome("tenet"))
# test(not is_palindrome("banana"))
# test(is_palindrome("straw warts"))
# test(is_palindrome("a"))
# test(is_palindrome(""))

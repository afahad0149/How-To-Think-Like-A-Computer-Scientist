import  sys

def replace(s, old, new):
    return new.join(s.split(old))

def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

test(replace("Mississippi", "i", "I") == "MIssIssIppI")
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
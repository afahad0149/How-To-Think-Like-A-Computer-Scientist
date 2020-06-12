import sys

#doing it without built in functions
def my_remove(sub, text):
	result = ""

	index = text.find(sub)
	if (index != -1):
		result = text[ : index] + text[index+len(sub) : ]
		return result

	return text

def my_remove_all(sub, text):
	result = my_remove(sub, text)

	while(result != text):
		text = result
		result = my_remove(sub, text) #makes result point out to a 
									  #new string object in every call
#"You can "update" an existing string by (re)assigning a variable to another string.
#The new value can be related to its previous value or to a completely different 
#string  altogether."

	return result


#using built-in functions:
def remove(sub, text):
	return text.replace(sub, "", 1)

def remove_all(sub, text):
	return text.replace(sub, "")

def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

# test(remove("an", "banana") == "bana")
# test(remove("cyc", "bicycle") == "bile")
# test(remove("iss", "Mississippi") == "Missippi")
# test(remove("eggs", "bicycle") == "bicycle")

# test(remove_all("an", "banana") == "ba")
# test(remove_all("cyc", "bicycle") == "bile")
# test(remove_all("iss", "Mississippi") == "Mippi")
# test(remove_all("eggs", "bicycle") == "bicycle")

# test(my_remove("an", "banana") == "bana")
# test(my_remove("cyc", "bicycle") == "bile")
# test(my_remove("iss", "Mississippi") == "Missippi")
# test(my_remove("eggs", "bicycle") == "bicycle")

test(my_remove_all("an", "banana") == "ba")
test(my_remove_all("cyc", "bicycle") == "bile")
test(my_remove_all("iss", "Mississippi") == "Mippi")
test(my_remove_all("eggs", "bicycle") == "bicycle")
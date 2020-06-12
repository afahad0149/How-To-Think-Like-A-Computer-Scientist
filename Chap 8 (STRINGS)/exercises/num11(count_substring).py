import sys

def count (search, text):
	cnt = 0
	index = text.find(search)

	while (index != -1):
		cnt += 1
		index = text.find(search, index+1)

	return cnt

#using the built in count method	
def count2 (search, text):
	return text.count(search)




def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("banana", "banana") == 1)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)
test(count("", "") == 1)
test(count("a","") == 0)
test(count("", "aaaaaa") == 7) #dunno why?

#consider the algorithm that checks if string is a substring. 
#The algorithm checks each character in the potential substring 
#and compares it to the corresponding character in the other string. 
#If any character does not match, then it is not a substring. 
#If the end of the searched string is reached, then it is a match. 
#In the case of an empty string, no character can differ 
#because there are no characters. The end is reached immediately 
#and the conclusion is that the empty string is a substring

test(count2("is", "Mississippi") == 2)
test(count2("an", "banana") == 2)
test(count2("banana", "banana") == 1)

#test(count2("ana", "banana") == 2) #FAIIIILLLLL!!!! Non-Overlapping substring
test(count2("ana", "banana") == 1)

test(count2("nana", "banana") == 1)
test(count2("nanan", "banana") == 0)

#test(count2("aaa", "aaaaaa") == 4) #FAAIIILLLLL!!!! Non-overlapping substring
test(count2("aaa", "aaaaaa") == 2)

test(count2("", "") == 1)
test(count2("a","") == 0)
test(count2("", "aaaaaa") == 7)


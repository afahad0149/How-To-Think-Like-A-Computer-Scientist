from unit_tester import *

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    split_list = s.split(old)
    word_list = []
    for i in split_list:
        if i != "":
            word_list.append(i)
    return new.join(word_list)


test(myreplace(",", ";", "this, that, and some other thing") == 
                         "this; that; and some other thing")
test(myreplace(" ", "**","Words will now    be   separated by stars.") ==
                         "Words**will**now**be**separated**by**stars.")
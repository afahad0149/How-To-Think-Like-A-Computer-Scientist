this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that)) # false as they are two different lists instances as lists are mutable
that = this # this and that refer to the same list which is the list this 
print("Test 2: {0}".format(this is that)) # true as they both point the same list

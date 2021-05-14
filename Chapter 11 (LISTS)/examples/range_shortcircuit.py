def f(n):
    """ Find the first positive integer between 101 and less
    than n that is divisible by 21
    """
    for i in range(101, n):
        if (i % 21 == 0):
             return i

print(f(110) == 105)
print(f(1000000000) == 105) #  if range were to eagerly go about building a list with all those elements,
                            # you would soon exhaust your computer’s available memory and crash the program

# lazy range wrapped in a call to list forces Python to turn
# the lazy promise into an actual list

print(list(range(10))) # Call in the promise, to produce a list

def swap(x, y):
    # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)

def correct_swap(x, y):     # a workaround to solve the swap problem
    (x, y) = (y, x)
    return (x, y)

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
#swap(a, b)
(a, b) = correct_swap(a, b)
print("after swap function call: a:", a, "b:", b)

# x is the alias of a anf y is the alias of b
# we have swapped the alaises so that now x points to y and y points to x
# a and b remains unchanged
# when the function is executed, x and y are destroyed so no effect on a and b


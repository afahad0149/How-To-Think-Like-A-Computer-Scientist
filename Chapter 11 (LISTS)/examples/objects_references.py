a = "banana"
b = "banana"

print(a == b)
# test whether two names refer to the same object using the is operator
print(a is b) 
# Since strings are immutable, 
# Python optimizes resources 
# by making two names that refer to the
#same string value refer to the same object.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
# a and b have the same value but do not refer to the same object
a = [1, 2, 3]
b = a[:]    # b is a clone of a
b[0] = 5

print(a) # [1, 2, 3]
print(b) # [5, 2, 3]
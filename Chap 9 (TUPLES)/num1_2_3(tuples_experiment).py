import math

def area (dim):
    area_rectangle = dim[0] * dim[1]
    area_circle = math.pi * dim[2] * dim[2]
    return (area_rectangle, area_circle)

rect, circle = area((2, 4, 2)) #works fineee if you enclose the tuples in parentheses
print (rect, circle)

#tuple is a generalization of a pair
#A pair is kind of a tuple

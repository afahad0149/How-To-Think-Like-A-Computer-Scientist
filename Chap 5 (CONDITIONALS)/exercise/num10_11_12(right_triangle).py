import math

def find_hypot (x,y):
	return (x ** 2 + y ** 2) ** 0.5

def is_rightangled (x, y, z):
	hyp_1 = max(max(x,y),z)

	if (hyp_1 == x):
		hyp_2 = find_hypot (y,z)

	elif (hyp_1 == y):
		hyp_2 = find_hypot (x,z)

	else:
		hyp_2 = find_hypot (y,x)

	return (abs(hyp_1-hyp_2) < 0.000001)




print (find_hypot(3.0,4.0))

print (is_rightangled(5.0, 3.0, 4.0))

print (is_rightangled(2.0, 3.0, 4.0))

print (is_rightangled(4.0, 5.0, 3.0))
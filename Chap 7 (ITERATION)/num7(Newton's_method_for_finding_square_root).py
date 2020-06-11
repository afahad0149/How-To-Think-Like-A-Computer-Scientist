import math

def Newton_sqrt(n):
	approx = n/2

	while True:
		better = (approx + n / approx) / 2
		print(better)

		if (abs(approx - better) < 0.00001):
			return better
		
		approx = better

#print(Newton_sqrt(1))
#print(Newton_sqrt(4)) 
#print(Newton_sqrt(9))
#print(Newton_sqrt(16))
#print(Newton_sqrt(25))
#print(Newton_sqrt(49.0))
#print(Newton_sqrt(81.0))
print(Newton_sqrt(2))



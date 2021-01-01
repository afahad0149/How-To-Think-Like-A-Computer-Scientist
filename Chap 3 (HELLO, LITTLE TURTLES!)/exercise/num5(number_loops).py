xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
sum = 0
product = 1

for i in xs:
	print(i,i*i)
	sum += i
	product *= i

print ("total =", sum, "product =", product)
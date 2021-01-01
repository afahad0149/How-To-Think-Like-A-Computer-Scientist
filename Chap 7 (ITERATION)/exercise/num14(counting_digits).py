def num_digits(n):
	count = 0;
	if (n==0 or n==-1):
		return 1

	else:
		while (n!=0 and n!=-1):
			count += 1
			n //= 10
		return count


# print (num_digits(0))
# print (num_digits(1))
# print (num_digits(11))
# print (num_digits(1122))

#print(-1//10, -1%10) #hence problem with negative integers

#print(-24//10) #result  = -3
#print(-3//10) #result = -1

print (num_digits(-24)) 
print (num_digits(-2)) 
print (num_digits(-1))
print (num_digits(-123456))

#print (0001230) #python cannot process numbers with leading zeros.
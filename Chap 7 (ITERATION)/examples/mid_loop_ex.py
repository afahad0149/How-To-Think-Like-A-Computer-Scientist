

def regular_loop():
	total = 0
	response = input("Enter the next number. (Leave blank to end):")

	while (response != ""):
		total += int(response)
		response = input("Enter the next number. (Leave blank to end):")

	print("The total of the numbers you entered is ", total)



def mid_loop():
	total = 0
	while True:
		response = input("Enter the next number. (Leave blank to end):")
		if (response == ""):
			break
		total += int(response)

	print("The total of the numbers you entered is ", total)

regular_loop()
mid_loop()
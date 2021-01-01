def find_grade (marks):
	if (marks >= 75):
		return "First"
	elif (marks >= 70):
		return "Upper Second"
	elif (marks >= 60):
		return "Second"
	elif (marks >= 50):
		return "Third"
	elif (marks >= 45):
		return "F1 Supp"
	elif (marks >= 40):
		return "F2"
	else:
		return "F3"

scores = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
			49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in scores:
	print (i, " = ", find_grade(i))
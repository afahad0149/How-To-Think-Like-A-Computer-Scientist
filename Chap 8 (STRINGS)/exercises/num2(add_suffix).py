prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	if letter in "OQ":
		print(letter + "uack")
	else:
		print(letter + suffix)
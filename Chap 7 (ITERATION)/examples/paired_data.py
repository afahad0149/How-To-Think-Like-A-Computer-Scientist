def example1():
	celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]

	print(celebs)
	print(len(celebs))

	for (nm,yr) in celebs:
		if (yr<1980):
			print(nm)


def example2():
	students = [("John",["CompSci", "Physics"]), 
				("Vuski", ["Maths", "CompSci", "Stats"]),
				("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
				("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
				("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

	for (name, courses) in students:
		print(name, "has taken", len(courses), "courses.")

	count = 0
	for (name, courses) in students:
		for i in courses:
			if i == "CompSci":
				count += 1

	print(count, "students have taken CompSci.")


#example1()
example2()
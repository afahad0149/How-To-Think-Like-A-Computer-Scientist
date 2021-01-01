def days_in_week (day):
	week = ["Sunday", "Monday", "Tuesday", "Wednesday",
			 "Thursday", "Friday", "Saturday"]
	return week[day]

day = int (input ("Enter the starting day number: "))
duration = int (input("Enter the duration of your stay: "))

day += duration
return_day = days_in_week (day % 7)

print ("Your return day is ", return_day)
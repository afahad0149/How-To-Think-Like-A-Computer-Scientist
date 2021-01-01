import sys
import math

#num 1:

def turn_clockwise(start):
	"""shows the direction after a 90 degree clockwise rotation"""

	if (start == "N"):
		return "E"
	elif (start == "E"):
		return "S"
	elif (start == "S"):
		return "W"
	elif (start == "W"):
		return "N"

#num 2:

def day_name(num):
	"""converts day number to corresponding day"""

	if (num >= 0 and num < 7):
		return days_in_week[num]

#num 3:

def day_num(day):
	"""converts day to corresponding day number"""

	for i in range(7):
		if days_in_week[i] == day:
			return i

#num 4:

def day_add(start_day, delta):
	"""finds the day, delta days from start_day"""

	day_reach = (day_num(start_day) + delta) % 7
	return day_name(day_reach)

#num 6:

def days_in_month(month):
	"""Finds the number of days in the given month"""
	
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	month_names = ["January", "February", "March", "April", "May", 
					"June", "July", "August", "September", "October",
					"November", "December"]
	for i in range(12):
		if (month_names[i] == month):
			return month_days[i]

#num 7:

def to_secs (hours, mins, secs):
	"""Calculates the total number of seconds passed (whole)"""

	total_secs = hours*60*60 + mins*60 + secs
	return int (total_secs)

#num 9:

def hours_in (secs):
	"""Calculates the number of hours passed (integer)"""

	hours = secs // (60*60)
	return hours

def minutes_in (secs):
	"""Calculates the number of minutes passed of the remaining seconds"""

	minutes = (secs % (60*60)) // 60
	return minutes

def seconds_in (secs):
	"""Calculates the number of seconds left"""

	seconds = secs % 60
	return seconds

#num 11:

def compare(a, b):
	"""compares two numbers and give respective outputs"""

	if (a > b):
		return 1
	elif(a == b):
		return 0
	else:
		return -1

#num 12:

def hypotenuse(opp, adj):
	"""returns the hypotenuse given two sides"""

	hyp = math.sqrt(opp ** 2 + adj ** 2)
	return hyp

#num 13:

def slope(x1, y1, x2, y2):
	"""returns the gradient of the line passing the points"""

	grad = (y2 - y1) / (x2 -x1)
	return grad

def intercept(x1, y1, x2, y2):
	"""returns the y-intercept of the line passing the points"""

	c = y1 - slope(x1, y1, x2, y2) * x1
	return c

#num 14:

def is_even(num):
	"""says if a number is even or odd"""

	if(num % 2 == 0):
		return True 
	else:
		return False

#num 15:

def is_odd(num):
	"""says if a number is odd or even"""

	if (is_even(num)):
		return False
	else:
		return True

#num 16:

def is_factor(f, n):
	"""says if f is a factor of n"""

	if (n % f == 0):
		return True
	else:
		return False


#num 17:

def is_multiple(mul, num):
	"""says if mul is a multiple of num"""

	return is_factor(num, mul)

#num 18:

def f2c(t):
	"""converts temperature in Fahrenheit to Celcius"""

	far = (t-32) * (5/9)
	return round(far)

#num 19:

def c2f(t):
	"""converts temperature in Celcius to Fahrenheit"""

	cel = (t * (9/5)) + 32
	return round(cel)


##############################  TEST SUITE ##############################################
def test (did_pass):
	"""Print the result of a test"""

	line_num = sys._getframe(1).f_lineno  #Get the caller's line number

	if (did_pass):
		msg = "Test at line {0} ok.".format(line_num)

	else:
		msg = "Test at line {0} FAILED.".format(line_num)

	print (msg)


def test_suite_1():
	"""Run the suite of tests for function in num1"""
	test(turn_clockwise("N") == "E")
	test(turn_clockwise("W") == "N")
	test(turn_clockwise(42) == None)
	test(turn_clockwise("rubbish") == None)

def test_suite_2():
	"""Run the suite of tests for function in num2"""
	test(day_name(3) == "Wednesday")
	test(day_name(6) == "Saturday")
	test(day_name(42) == None)

def test_suite_3():
	"""Run the suite of tests for function in num3"""
	test(day_num("Friday") == 5)
	test(day_num("Sunday") == 0)
	test(day_num(day_name(3)) == 3)
	test(day_name(day_num("Thursday")) == "Thursday")
	test(day_num("Halloween") == None)

def test_suite_4():
	"""Run the suite of tests for function in num4"""
	test(day_add("Monday", 4) == "Friday")
	test(day_add("Tuesday", 0) == "Tuesday")
	test(day_add("Tuesday", 14) == "Tuesday")
	test(day_add("Sunday", 100) == "Tuesday")
	test(day_add("Sunday", -1) == "Saturday")
	test(day_add("Sunday", -7) == "Sunday")
	test(day_add("Tuesday", -100) == "Sunday")

def test_suite_5():
	"""Run the suite of tests for function in num5"""
	test(days_in_month("February") == 28)
	test(days_in_month("December") == 31)
	test(days_in_month("Ramen") == None)
	test(days_in_month("Boishakh") == None)

def test_suite_7():
	"""Run the suite of tests for function in num7"""
	test(to_secs(2, 30, 10) == 9010)
	test(to_secs(2, 0, 0) == 7200)
	test(to_secs(0, 2, 0) == 120)
	test(to_secs(0, 0, 42) == 42)
	test(to_secs(0, -10, 10) == -590)
	test(to_secs(2.5, 0, 10.71) == 9010)
	test(to_secs(2.433,0,0) == 8758)

def test_suite_9():
	"""Run the suite of tests for function in num9"""
	test(hours_in(9010) == 2)
	test(minutes_in(9010) == 30)
	test(seconds_in(9010) == 10)

def test_suite_11():
	"""Run the suite of tests for function in num11"""
	test(compare(5, 4) == 1)
	test(compare(7, 7) == 0)
	test(compare(2, 3) == -1)
	test(compare(42, 1) == 1)

def test_suite_12():
	"""Run the suite of tests for function in num12"""
	test(hypotenuse(3, 4) == 5.0)
	test(hypotenuse(12, 5) == 13.0)
	test(hypotenuse(24, 7) == 25.0)
	test(hypotenuse(9, 12) == 15.0)

def test_suite_13a():
	"""Run the suite of tests for function in num113"""
	test(slope(5, 3, 4, 2) == 1.0)
	test(slope(1, 2, 3, 2) == 0.0)
	test(slope(1, 2, 3, 3) == 0.5)
	test(slope(2, 4, 1, 2) == 2.0)

def test_suite_13b():
	"""Run the suite of tests for function in num113"""
	test(intercept(1, 6, 3, 12) == 3.0)
	test(intercept(6, 1, 1, 6) == 7.0)
	test(intercept(4, 6, 12, 8) == 5.0)

def test_suite_14():
	"""Run the suite of tests for function in num14"""
	test(is_even(2)==True)
	test(is_even(0)==True)
	test(is_even(-5)==False)
	test(is_even(1)==False)

def test_suite_15():
	"""Run the suite of tests for function in num15"""
	test(is_odd(2)==False)
	test(is_odd(0)==False)
	test(is_odd(-5)==True)
	test(is_odd(1)==True)
	test(is_odd(99)==True)

def test_suite_16():
	"""Run the suite of tests for function in num16"""
	test(is_factor(3, 12))
	test(not is_factor(5, 12))
	test(is_factor(7, 14))
	test(not is_factor(7, 15))
	test(is_factor(1, 15))
	test(is_factor(15, 15))
	test(not is_factor(25, 15))

def test_suite_17():
	"""Run the suite of tests for function in num17"""
	test(is_multiple(12, 3))
	test(is_multiple(12, 4))
	test(not is_multiple(12, 5))
	test(is_multiple(12, 6))
	test(not is_multiple(12, 7))

def test_suite_18():
	"""Run the suite of tests for function in num18"""
	test(f2c(212) == 100) # Boiling point of water
	test(f2c(32) == 0) # Freezing point of water
	test(f2c(-40) == -40) # Wow, what an interesting case!
	test(f2c(36) == 2)
	test(f2c(37) == 3)
	test(f2c(38) == 3)
	test(f2c(39) == 4)

def test_suite_19():
	"""Run the suite of tests for function in num19"""
	test(c2f(0) == 32)
	test(c2f(100) == 212)
	test(c2f(-40) == -40)
	test(c2f(12) == 54)
	test(c2f(18) == 64)
	test(c2f(-48) == -54)

days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", 
					"Thursday", "Friday", "Saturday"]
#test_suite_1()
#test_suite_2()
#test_suite_3()
#test_suite_4()
#test_suite_5()
#test_suite_7()
#test_suite_9()
#test_suite_11()
#test_suite_12()
#test_suite_13a()
#test_suite_13b()
#test_suite_14()
#test_suite_15()
#test_suite_16()
#test_suite_17()
#test_suite_18()
test_suite_19()
import calendar

#1_a
cal = calendar.TextCalendar()
#cal.pryear(2012) # prints the entire calendar(days and mobths) of the year 2012

#1_b
cal2 = calendar.TextCalendar(firstweekday = 3)
#cal2.prmonth(2021, 10)

#1_c
def print_month(date):
    month_start = date.find('-')
    month_end = date.find('-', month_start + 1)
    month = int(date[month_start + 1 : month_end])
    year = 2021
    cal.prmonth(year, month)

#print_month("20-10-1995")

#1_d
d = calendar.LocaleTextCalendar(6, locale="bn_BD.utf8")
#d.pryear(2012)

# d = calendar.LocaleTextCalendar(6, "ENGLISH")
# d.pryear(2012) # locale.Error: unsupported locale setting

#1_e
print(calendar.isleap(2012))
print(calendar.isleap(2002))
# Takes year as an argument, returns true if the year is a leap year. 
# It is a pure function; the return value only depends on the year not any states of calendar object

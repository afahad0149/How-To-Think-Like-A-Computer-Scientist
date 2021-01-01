cur_time = int (input("Enter current time (in hours): "))

wait = int (input("Enter waiting time (in hours): "))

alarm_time = (cur_time + wait) % 24

print ("The alarm goes off at", alarm_time, "00")
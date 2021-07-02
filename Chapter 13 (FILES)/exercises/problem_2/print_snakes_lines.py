f = open("snakes.txt", "r")

lines = f.readlines()

for line in lines:
    lower_line = line.lower()
    if lower_line.find("snake") != -1:
        print(line, end="")

f.close()
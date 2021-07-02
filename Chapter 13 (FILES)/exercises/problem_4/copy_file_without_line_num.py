inp_f = open("source.txt", "r")
out_f = open('destination.txt', "w")

lines = inp_f.readlines()

for line in lines:
    out_f.write(line[5:])

inp_f.close()
out_f.close()
inp_f = open("source.txt", "r")
out_f = open("destination.txt", "w")

lines = inp_f.readlines()

line_num = 1
for line in lines:
    out_f.write("{:0>4d} ".format(line_num) + line)
    line_num += 1

inp_f.close()
out_f.close()
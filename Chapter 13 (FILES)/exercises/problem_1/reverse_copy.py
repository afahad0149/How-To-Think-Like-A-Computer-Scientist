inp_f = open('source.txt', 'r')
out_f = open('destination.txt', 'w')

lines = inp_f.readlines()

for i in range (-1, -len(lines)-1, -1):
    out_f.write(lines[i])

inp_f.close()
out_f.close()
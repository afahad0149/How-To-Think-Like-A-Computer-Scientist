f = open("Runaway- Aurora.txt")
content = f.read()
f.close()

words = content.split()
print("There are {0} words in the file".format(len(words)))
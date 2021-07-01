f = open("somefile.zip", "rb")  # added a "b" to the mode to tell Python
                                # that the files are binary rather than text files
g = open("thecopy.zip", "wb")

while True:
    buf = f.read(1024)  # read can take an argument which tells it 
                        # how many bytes to attempt to read from the file and store in the buffer
    if len(buf) == 0:
        break
    g.write(buf)

f.close()
g.close()
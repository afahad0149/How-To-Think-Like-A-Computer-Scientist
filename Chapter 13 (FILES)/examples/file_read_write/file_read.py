file_handle = open("/home/afahad/Git_Repositories/How-To-Think-Like-A-Computer-Scientist/Chapter 13 (FILES)/examples/file_read_write/test.txt", "r")
while True:
    line = file_handle.readline()
    if len(line) == 0:
        break
    print(line, end = "")   # suppress the newline character that print usually appends to our strings
                            # as each line has its own newliine character

file_handle.close()
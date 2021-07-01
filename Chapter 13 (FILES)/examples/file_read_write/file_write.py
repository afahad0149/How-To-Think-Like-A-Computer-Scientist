myfile = open("/home/afahad/Git_Repositories/How-To-Think-Like-A-Computer-Scientist/Chapter 13 (FILES)/examples/file_read_write/test.txt", "w")

myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")

myfile.close()
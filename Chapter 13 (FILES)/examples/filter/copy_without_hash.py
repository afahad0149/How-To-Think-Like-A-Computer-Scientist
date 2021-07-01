# a filter that copies one file to another, omitting any lines that begin with #

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue
        # Put any more processing logic here
        outfile.write(text)
    infile.close()
    outfile.close()

filter('text_with_hash.txt', 'copy_without_hash.txt')
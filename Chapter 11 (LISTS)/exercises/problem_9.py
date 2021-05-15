song = "The rain in Spain..."
print(" ".join(song.split()))
# split creates an array of words seperated by ANY NUMBER OF SPACES (delimiter).
# join with the seperator " " concatenates each of the words followed by a SINGLE SPACE (except the last word)

# A case where they would be different
song = " The rain  in Spain... "
print(" ".join(song.split()))
print(song)

# the seperator is fixed but the delimiter might not be in case of WHITE SPACES
# takes a string as input and returns a string with only alphanumeric characters
def cleanword(word):
    cleaned = ""
    for char in word:
        if char.isalnum():
            cleaned += char

    return cleaned

# returns False if the input string has extra dashes
def has_dashdash(str):
    ind = str.find("--")
    if ind == -1:
        return False
    return True

# extract words (lowercase) from a sentence and returns them as a list
def extract_words(phrase):
    lower_phrase = phrase.lower()
    no_spaces = lower_phrase.split()
    word_list = []
    for item in no_spaces:
        words = item.split("--")
        for word in words:
            word_list.append(cleanword(word))
    
    return word_list

# returns the number of instances of the input word in the input word list
def wordcount(word, word_list):
    count = 0
    for item in word_list:
        if word == item:
            count += 1

    return count 

# returns the set of words from the input word list
def wordset(word_list):
    word_set = []
    for item in word_list:
        if item not in word_set:
            word_set.append(item)
    
    word_set.sort()
    return word_set


# returns the longest word in the input word set
def longestword(word_set):
    word_set.sort(reverse=True, key= lambda x:len(x))
    if word_set == []:
        return 0
    else:
        return len(word_set[0])

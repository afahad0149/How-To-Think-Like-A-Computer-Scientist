#remove punctuation and split the resulting string in to a list of words

import string

#punctuation = "!\"#$%&’()*+,-./:;<=>?@[\\]^_‘{|}~"

def remove_punctuation(s):
	s_sans_punct = ""
	for ch in s:
		if ch not in string.punctuation:
			s_sans_punct += ch

	return s_sans_punct

print(remove_punctuation('"Well, I never did!", said Alice.'))
print(remove_punctuation("Are you very, very, sure?"))

my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake’s
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The ’extra stuff’ gets passed out as ---
you guessed it --- snake POOP! """

words = remove_punctuation(my_story).split()
print(words)
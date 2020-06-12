import string

def remove_punctuations(text):
	new_str = ""
	for ch in text:
		if ch not in string.punctuation:
			new_str += ch

	return new_str

def word_frequency (text, letter):
	words = text.split()
	total_words = len(words)
	words_with_letter = 0

	for word in words:
		if letter in word:
			words_with_letter += 1

	frequency = (words_with_letter/total_words)*100

	print ("Your text contains {0} words, of which {1} ({2:.2f}%) contain an '{3}'.".
			format(total_words, words_with_letter, frequency, letter))


text = """“Voilà! 
			In view, a humble vaudevillian veteran cast vicariously as both victim 
			and villain by the vicissitudes of Fate. This visage, no mere veneer of vanity,
			is a vestige of the vox populi, now vacant, vanished. 
			However, this valorous visitation of a bygone vexation stands vivified 
			and has vowed to vanquish these venal and virulent vermin 
			vanguarding vice and vouchsafing the violently vicious 
			and voracious violation of volition! The only verdict is vengeance; 
			a vendetta held as a votive, not in vain, 
			for the value and veracity of such shall one day vindicate 
			the vigilant and the virtuous. [laughs] Verily, this vichyssoise of verbiage 
			veers most verbose, so let me simply add that 
			it’s my very good honor to meet you and you may call me “V”."""

no_punct_text = remove_punctuations(text)
#print(no_punct_text)
word_frequency(no_punct_text,'e')
word_frequency(no_punct_text,'v')			
#removes vowels from the strings.

def remove_vowels(s):
	vowels = "aeiouAEIOU"
	res_str = ""

	for char in s:
		if char not in vowels:
			res_str += char

	return res_str

print(remove_vowels("Akib Ahmed Fahad"))
print(remove_vowels("compsci"))
print(remove_vowels("aAbEefIijOopUus"))
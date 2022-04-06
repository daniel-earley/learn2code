# Make a function that will find every vowel in a string
# vowels = ['a','e','i','o','u']
# example: findVowels("apple") returns a = 1, e = 1, i = 0, o = 0, u = 0

# Hints
# word = "apple"
# print(word[0])
# for letter in word:
# 	print(letter)

def findVowels(word):
	vowels ={"a":0, "e":0, "i":0, "o":0, "u":0}
	for letter in word:
		if letter == 'a':
			vowels["a"] += 1
		elif letter == "e":
			vowels["e"] += 1
		elif letter == "i":
			vowels["i"] += 1
		elif letter == "o":
			vowels["o"] += 1
		elif letter == "u":
			vowels["u"] += 1
	
	return vowels

print(findVowels("Hello"))

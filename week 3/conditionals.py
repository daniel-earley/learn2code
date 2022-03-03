word = "boxx"

if word == "box":
	print(word)
elif word == "boxx":
	print(word)
else:
	print("word doesn't equal box")

num1 = 11

if (num1 % 2 == 0):
	print("is even")
else:
	print("is odd")

# Scope
# the scope of a block of code, in python, is determined by the indentation
# the scope of code determines where that code belongs to

if num1 < 5:
	# scope starts
	a = 0
	print(a)
	# scope ends
else:
	print("a does not yet exist")
	# print(a)

num2 = 20

if (num1 > num2) or (num1 < num2):
	print("Hello")

if (num1 >= 10) and (num2 <= 10):
	print("World")
else:
	print("And requires all inputs to be true")

isEven = False
if (num2 % 2 == 0):
	isEven = True
	print(not isEven)

if (num2 % 2 == 0):
	isEven = True

if not isEven:
	print("it is odd")
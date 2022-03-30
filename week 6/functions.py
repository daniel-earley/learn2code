from functools import cache

# This is a function with no parameters
def helloWorld():
	print("hello world")

# This is a function with parameters
def add(num1, num2):
	return num1 + num2

# This function is recursive because it calls itself within it's block of code
@cache
def fib(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1;
	else:
		return fib(num-1) + fib(num-2)

# This is a function with different parameter types
def calculator(num1, symbol, num2):
	if (symbol == "+"):
		return num1 + num2
	elif (symbol == "-"):
		return num1 - num2
	elif (symbol == "*"):
		return num1 * num2
	elif (symbol == "/"):
		return num1 / num2

# This is a function with a default argument for its parameter
def printWord(word="default word"):
	print(word)

# ~~~ Call Functions ~~~

helloWorld()

# The values passed to the function are called arguments
number = add(5, 5)
print(number)

# 1,1,2,3,5,8,13
print(fib(7))

print(calculator(100, "/", 10))

printWord()
	
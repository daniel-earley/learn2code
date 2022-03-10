'''
# Initialize boolean variable
positiveNumber = True

# Initialize a number variable
num = 0

# Initalize a string variable
userInput = ""

# While Loop
while positiveNumber == True:
	# Prompt
	print("Please enter a positive number:")
	
	# Get user input from terminal
	userInput = input()
	
	# Typecast to an integer and set num = userInput
	num = int(userInput)

	# Conditional
	if num < 0:
		positiveNumber = False
'''

# Initialize a number variable
num = 0

# While loop
while num >= 0:
	# Prompt
	print("Please enter a positive number:")

	# Get user input and typecast to integer
	num = int(input())


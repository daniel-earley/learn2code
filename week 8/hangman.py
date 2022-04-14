import random

class Player:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.lives = 5

    # Getters and Setters
    def getName(self):
        return self.name
    
    def getLives(self):
        return self.lives
    
    def setLives(self, lives):
        self.lives = lives

    # Subtract 1 from the number of lives
    def decLives(self):
        self.lives -= 1
    
    # Check if the number of lives are greater than 0
    def isAlive(self):
        if self.lives > 0:
            return True
        else:
            return False

class Word:
    # Constructor
    def __init__(self):
        self.word = ""
        self.letters=[]
        self.oldLetters=[]

        # Open the words file
        with open('words.txt') as file:
            line = file.readline()
        self.wordList = line.split(",")

    # Getters and Setters
    def setWord(self):
        # This function gets a random word from the wordlist
        index = random.randint(0, len(self.wordList)-1)
        self.word = self.wordList[index]

    def getWord(self):
        return self.word

    def getOldLetters(self):
        return self.oldLetters

    # Checks if the letter has already been input or not
    def checkOldLetter(self, letter):
        if self.oldLetters.__contains__(letter):
            return True
        else: 
            return False

    # Print the "_" version of the word
    def printHidden(self):
        # create a list of the string for example: "word" -> ["w", "o", "r", "d"]
        temp = list(self.word)
        for i in range(len(temp)):
            # if the letter is not in the letters list and the letter isn't a space (" ") then replace it with "_"
            if not temp[i] in self.letters and temp[i] != " ":
                temp[i] = "_"
        # print the list as a string using join()
        print("".join(temp))
                    
    # Checks if the input letter is in the word
    def checkLetter(self, letter):
        # Convert the word to uppercase 
        temp = self.word.upper()

        # Checks if the input letter (changed to uppercase) is in the word
        if temp.__contains__(letter.upper()):
            # Add the letter to the letter list and old letter list
            self.letters.append(letter.lower())
            self.oldLetters.append(letter.lower())
            return True
        else:
            # Add the letter to the old letter list
            self.oldLetters.append(letter.lower())
            return False
    
    # Check if all of the letters have been found
    def allLetters(self):
        # Compares the length of the list of letters to the length of the string word
        if len(self.letters) == len(self.word):       
            return True
        else:
            return False

    # To string function to print the word
    def __str__(self):
        return self.word





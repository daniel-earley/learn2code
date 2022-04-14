from hangman import *

word = Word()

# Booleans
alive = True
newGame = True

# Create a player
userInput = input("Enter username: ")
player = Player(userInput)

while alive:
    # set the word
    if newGame:
        word.setWord()
        newGame = False
    
    # Print the hidden word
    word.printHidden()

    # Get user input
    userInput = input("Please enter a letter: ")

    # check the letter
    if word.checkOldLetter(userInput) == False:
        if not word.checkLetter(userInput):
            player.decLives()
            print(f"{player.getName()} has {player.getLives()} lives left")
    else:
        print(f"You've already played these letters {word.getOldLetters()}")
    
    # Check if the player still has lives left
    if (player.isAlive() == False):
        print(f"{player.getName()} is out of lives")
        alive = player.isAlive()
        break
    
    # Check if the player has guessed all the correct letters
    if word.allLetters():
        print(f"{player.getName()} Wins!")
        break
    
    
    


    
    


from words import word_list
import random
import re


def startHangman():
    print(" ")
    print("Press 1 for single player \nPress 2 for multiplayer")
    mode = input("Mode: ")
    if(mode == "1" or mode == "2"):
        if(int(mode) == 1):
            word = get_words()
        elif(int(mode) == 2):
            word = twoPlayer()
        print("enter (`) as guess to exit")    
        play(word)

    else:
        print("invalid mode, enter 1 or 2\n")
        startHangman()    

def get_words():
    word = random.choice(word_list)
    return word.upper()

def twoPlayer():
    guessedCharacter = input("Player One pick a word for your opponent: ")
    return guessedCharacter.upper()

def showGuesses(guessed_letters,guessed_words):
    guessedLetter = ", ".join(guessed_letters)
    guessedWord = ", ".join(guessed_words)
    print("Guessed Letters: " + guessedLetter + "\nGuessed Words: " + guessedWord)
    #print(String(guessed_letters))
    
    #print(guessed_words)

def play(word):
    word_completion = "_ " * len(word)
    if " " in word:
        temp_word_as_list =  list(word_completion)
        after_spaces_added = []
        spacePlaces = re.finditer(" ", word) # find indexes of spaces
        space_positions = [match.start() for match in spacePlaces]
        for i in space_positions:  # adds spaces where indexs are from previous step
            temp_word_as_list[i * 2] = " "  
        for i in range(0, (len(temp_word_as_list) - 1), 2): # list -> string
            after_spaces_added.append((temp_word_as_list[i]))
        word_completion = " ".join(after_spaces_added)

            
        
    
    guessed =  False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries != 0:
        word_as_list =  list(word_completion)
        guessedCharacter = input("Guess a Character: ")
        guessedCharacter = guessedCharacter.upper()
        
        if(guessedCharacter == "`"):
                tries = 0
        if(len(guessedCharacter) == 1 and guessedCharacter.isalpha()):
            
            if(guessedCharacter) in guessed_letters:
                print("You already guessed this character!")
            elif(guessedCharacter not in word):
                print("Try it again!")
                guessed_letters.append(guessedCharacter)
                tries =  tries - 1
            else:
                print("Nice, you got one")
                guessed_letters.append(guessedCharacter)
                #word_as_list =  list(word_completion)
                duplicates = re.finditer(guessedCharacter, word) 
                duplicates_positions = [match.start() for match in duplicates]
                for index in duplicates_positions:
                    word_as_list[index * 2] = guessedCharacter
                
        elif(len(guessedCharacter) == len(word)):
            #print("here: " + guessedCharacter)
            if(guessedCharacter) in guessed_words:
                print("You already guessed this word!")
            elif(guessedCharacter != word):
                print("Try it again!")
                guessed_words.append(guessedCharacter)
                tries =  tries - 1
            else:
                
                guessed_words.append(guessedCharacter)
                #word_as_list =  list(word_completion)
                #index_of_guessedChar = word.index(guessedCharacter)
                #word_as_list[index_of_guessedChar] = guessedCharacter
                word_as_list = guessedCharacter
                guessed  = True
        else:
            print("invalid character or word is not long enough")
        
        #word_as_list =  list(word_completion)
        word_completion = "".join(word_as_list)
        print(display_hangman(tries))
        showGuesses(guessed_letters,guessed_words)
        print(word_completion)
        print("\n")
        if "_" not in word_completion:
            guessed = True
    if tries > 0:        
        print("Winner, you got it!\n")
    else:
        print("You Lost!")

    
    


        


def display_hangman(tries):
    stages = [  
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
    
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
    
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
    
    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
    
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
    
    """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
    
    """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


if __name__ == "__main__":
    startHangman()
from hangman import *
from tictactoe import *
from blackjack import *
from displayArt import *

def main():
    welcome()
    game = input("Press 1 for hangman.\nPress 2 for tic tac toe\nPress 3 for blackjack\nPress 4 to quit\nMode: ")
    if game == "1":
        welcomeHM()
        startHangman()
    elif game == "2":
        welcomeTTT()
        startTic()
    elif game == "3":
        welcomeBJ()
        startBlackJack()
    elif game == "4":
        return
    else:
        print("\ninvalid input, enter a valid mode\n")
        main()    

if __name__ == "__main__":
    main()
import random

def startTic():
    #finished = False
    #theBoard["1"] = "x"
    #theBoard["2"] = " "
    #theBoard["3"] = " "
    #theBoard["4"] = " "
    #theBoard["5"] = "x"
    #theBoard["6"] = " "
    #theBoard["7"] = " "
    #theBoard["8"] = " "
    #theBoard["9"] = "x"
    print(" ")
    active = True
    list_of_num_left = [1,2,3,4,5,6,7,8,9]
    print("Example board below. Each number corresponds to a tile\n")
    printBoard(theBoardExample)
    print(" ")  
    while checkFinished(theBoard) == False and active == True:
        pick = input("Pick a Location: ")
        invalidKey = False
        if pick ==  "`":
            active = False # stops game
        elif pick == "1" and 1 in list_of_num_left:
            theBoard["1"] = "x"
            list_of_num_left.remove(1)
        elif pick == "2" and 2 in list_of_num_left:
            theBoard["2"] = "x"
            list_of_num_left.remove(2)
        elif pick == "3" and 3 in list_of_num_left:
            theBoard["3"] = "x"
            list_of_num_left.remove(3)
        elif pick == "4" and 4 in list_of_num_left:
            theBoard["4"] = "x"
            list_of_num_left.remove(4)
        elif pick == "5" and 5 in list_of_num_left:
            theBoard["5"] = "x"
            list_of_num_left.remove(5)
        elif pick == "6" and 6 in list_of_num_left:
            theBoard["6"] = "x"
            list_of_num_left.remove(6)
        elif pick == "7" and 7 in list_of_num_left:
            theBoard["7"] = "x"
            list_of_num_left.remove(7)
        elif pick == "8" and 8 in list_of_num_left:
            theBoard["8"] = "x"
            list_of_num_left.remove(8)
        elif pick == "9" and 9 in list_of_num_left:
            theBoard["9"] = "x" 
            list_of_num_left.remove(9)
        else:
            #call method again
            invalidKey = True
            print("Invalid Key")
        if(invalidKey == False):
            cpuPick = random.choice(list_of_num_left) # change from random pick to AI
            theBoard[str(cpuPick)] = "o"
            list_of_num_left.remove(cpuPick)

        print(" ")
        printBoard(theBoard)
        print(" ")

        #print(list_of_num_left) # remove after done

        


        #next work on user inp and place on board the cpu repeat til true
        #print(checkFinished(theBoard))
theBoardExample = {'1': '1' , '2': '2' , '3': '3' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '7': '7' , '8': '8' , '9': '9' }

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
            
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
 
def checkFinished(board):
    if(check_rows(board) == True or check_rows_cpu(board) == True or check_cols(board) == True or check_cols_cpu(board) == True or check_diags(board) == True or check_diags_cpu(board) == True):
        return True
    else:
        return False

def check_rows(board):
    for box in board:
        if board["1"] == "x" and board["2"] == "x" and board["3"] == "x":
            print("winner")
            return True
        elif board["4"] == "x" and board["5"] == "x" and board["6"] == "x":
            print("winner")
            return True
        elif board["7"] == "x" and board["8"] == "x" and board["9"] == "x":
            print("winner")
            return True
    return False

def check_cols(board):
    for box in board:
        if board["1"] == "x" and board["4"] == "x" and board["7"] == "x":
            print("winner")
            return True
        elif board["2"] == "x" and board["5"] == "x" and board["8"] == "x":
            print("winner")
            return True
        elif board["3"] == "x" and board["6"] == "x" and board["9"] == "x":
            print("winner")
            return True
    return False

def check_diags(board):
    for box in board:
        if board["1"] == "x" and board["5"] == "x" and board["9"] == "x":
            print("winner")
            return True
        elif board["3"] == "x" and board["5"] == "x" and board["7"] == "x":
            print("winner")
            return True
    return False

def check_rows_cpu(board):
    for box in board:
        if board["1"] == "o" and board["2"] == "o" and board["3"] == "o":
            print("you lose")
            return True
        elif board["4"] == "o" and board["5"] == "o" and board["6"] == "o":
            print("you lose")
            return True
        elif board["7"] == "o" and board["o"] == "x" and board["o"] == "x":
            print("you lose")
            return True
    return False

def check_cols_cpu(board):
    for box in board:
        if board["1"] == "o" and board["4"] == "o" and board["7"] == "o":
            print("you lose")
            return True
        elif board["2"] == "o" and board["5"] == "o" and board["8"] == "o":
            print("you lose")
            return True
        elif board["3"] == "o" and board["6"] == "o" and board["9"] == "o":
            print("you lose")
            return True
    return False

def check_diags_cpu(board):
    for box in board:
        if board["1"] == "o" and board["5"] == "o" and board["9"] == "o":
            print("you lose")
            return True
        elif board["3"] == "o" and board["5"] == "o" and board["7"] == "o":
            print("you lose")
            return True
    return False

if __name__ == "__main__":
    startTic()
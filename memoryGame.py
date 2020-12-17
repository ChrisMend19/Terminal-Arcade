import rand

def startMemory():
    printBoard()



def printBoard():

    list_of_turns = []
    active = true
    while active == true:
        turn = random.randint(1,4)

    x = "1"
    y = "2"
    z = "3"
    w = "4"

    board = {'1': x , '2': y , '3': z ,
            '4': w }

    print(board['1'] + '     |     ' + board['2'])
    #print('-+-+-')
    print(board['1'] + '     |     ' + board['2'])
    print('-+-+-   ' + '-+-+-')
    print(board['3'] + '     |     ' + board['4'])
    print(board['3'] + '     |     ' + board['4'])

    



if __name__ == "__main__":
    startMemory()
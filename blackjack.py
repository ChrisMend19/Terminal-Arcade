import random

def startBlackJack():
    print("\nsimplified blackjack. Does not contain every specific rule just the basics.\nEnter '`' as action to exit.\n")
    list_of_cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A",
                    "2","3","4","5","6","7","8","9","10","J","Q","K","A",
                    "2","3","4","5","6","7","8","9","10","J","Q","K","A",
                    "2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    list_of_cards_temp = ["A","K","Q","A","K","Q"]
    totalHand = 0
    dealerTotal = 0
    yourHand = []
    dealerHand = []
    
    
    firstCard = (hit(list_of_cards))
    yourHand.append(firstCard) # add first 2 cards to user
    secondCard = (hit(list_of_cards))
    yourHand.append(secondCard)

    dealerFirstCard = (hit(list_of_cards))
    dealerHand.append(dealerFirstCard) # add first 2 cards to cpu
    dealerSecondCard = (hit(list_of_cards))
    dealerHand.append(dealerSecondCard)

    if(firstCard == "J" or firstCard == "Q" or firstCard =="K"): #check if cards are royal if so changes value to number
        firstCard = 10
    if(secondCard == "J" or secondCard == "Q" or secondCard =="K"):
        secondCard = 10
    if(firstCard == "A"):
        hand_as_string = "".join(str(yourHand))
        print("your hand: " + hand_as_string)
        aceNumber = ace()
        while (aceNumber != "1" or aceNumber != "11"):
            if aceNumber == "1" or aceNumber == "11":
                break
            aceNumber = ace()
        firstCard = aceNumber
        
    if(secondCard == "A"):
        hand_as_string = "".join(str(yourHand))
        print("your hand: " + hand_as_string)
        aceNumber = ace()
        while (aceNumber != "1" or aceNumber != "11"):
            if aceNumber == "1" or aceNumber == "11":
                break
            aceNumber = ace()
        secondCard = aceNumber
    
    if(dealerFirstCard == "J" or dealerFirstCard == "Q" or dealerFirstCard =="K"):
        dealerFirstCard = 10
    if(dealerSecondCard == "J" or dealerSecondCard == "Q" or dealerSecondCard=="K"):
        dealerSecondCard = 10   
    if(dealerFirstCard == "A"):
        dealerFirstCard = 1
    if(dealerSecondCard == "A" and (dealerFirstCard + 11) <= 21):
        dealerSecondCard = 11
    elif dealerSecondCard == "A":
        dealerSecondCard = 1
       
    totalHand = int(firstCard) + int(secondCard)
    dealerTotal = int(dealerFirstCard) + int(dealerSecondCard)
    
    while(totalHand <= 21):
        
        print("your total: " + str(totalHand) + "\n")

        hand_as_string = "".join(str(yourHand))
        print("your hand: " + hand_as_string)
        #print("your total: " + str(totalHand))
    
        dealerHand_as_string = "".join(str(dealerHand))
        print("dealer has: " + dealerHand_as_string)
        #print("dealer total: " + str(dealerTotal))
        print(" ")
        choice = input("Would you like to 'hit' or 'stand'? ")
        print(" ")
        if(choice == "`"):
            return
        # hold
        if(choice == "stand"): # get cpu hand
            while(dealerTotal < 17):
                dealerNextCard = (hit(list_of_cards))
                dealerHand.append(dealerNextCard)
                if dealerNextCard == "J" or dealerNextCard == "Q" or dealerNextCard == "K":
                    dealerNextCard = 10
                elif dealerNextCard == "A":
                    if(dealerTotal + 11) <= 21:
                        dealerNextCard = 11
                    else:
                        dealerNextCard = 1    
                dealerTotal += int(dealerNextCard)
            #dealerHand_as_string = "".join(str(dealerHand))
            #print("dealer's final hand: " + dealerHand_as_string) 
            #print("D: " + str(dealerTotal) + "U: " + str(totalHand))
            if dealerTotal == totalHand:
                print("Draw")
                hand_as_string = "".join(str(yourHand)) #fix dealer total its not winning  correctly
                dealerHand_as_string = "".join(str(dealerHand))
                print("your hand: " + hand_as_string)
                print("dealer's final hand: " + dealerHand_as_string + "\n") 
                return
            elif dealerTotal < totalHand:
                print("You outwitted your opponent, You Win!")
                hand_as_string = "".join(str(yourHand))
                dealerHand_as_string = "".join(str(dealerHand)) 
                print("your hand: " + hand_as_string)
                print("dealer's final hand: " + dealerHand_as_string + "\n")
                return
            elif dealerTotal > 21:
                print("Dealer busted, You Win!")
                hand_as_string = "".join(str(yourHand))
                dealerHand_as_string = "".join(str(dealerHand))
                print("your hand: " + hand_as_string)
                print("dealer's final hand: " + dealerHand_as_string + "\n") 
                return
            else:
                print("You Lose")
                hand_as_string = "".join(str(yourHand))
                dealerHand_as_string = "".join(str(dealerHand))
                print("your hand: " + hand_as_string)
                print("dealer's final hand: " + dealerHand_as_string + "\n") 
                return
            
        # hit
        if(choice == "hit"):
            nextCard = (hit(list_of_cards))
            yourHand.append(nextCard)
            if nextCard == "J" or nextCard == "Q" or nextCard =="K":
                nextCard = 10
            if nextCard == "A":
                aceNum = ace()
                nextCard = aceNum
            totalHand += int(nextCard)
            continue

         
    if(totalHand > 21):
        hand_as_string = "".join(str(yourHand))
        print("your hand: " + hand_as_string + "\n")
        print("you busted, you lost")   
        



        #totalHand += int(hit(list_of_cards))
        #print(totalHand)
    

def hit(list_of_cards):
    yourCard = random.choice(list_of_cards) 
    list_of_cards.remove(yourCard)
    return yourCard

def cpu_hit_until_17(dealerHand,list_of_cards):
    while(sum(dealerHand) < 17):
        dealerNextCard = int(hit(list_of_cards))
        dealerHand.append(dealerNextCard)
        dealerTotal += dealerNextCard
    return dealerHand

def ace():
    aceNum = input("you have a ace, do you want a '1' or '11': ")
    return aceNum

if __name__ == "__main__":
    startBlackJack()
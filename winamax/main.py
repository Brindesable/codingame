import sys
import math

def getCardVal(card):
    """
    Give a value for each card. In this game, the color doesn't matter. We give a numeric value for the cards above 10.
    """
    cardVal = {'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
    val = 0
    if(card[0].isdigit()):
        val = int(card[0])
        if(card[1] == '0') :
            val = 10
    elif(card[0].isalpha()):
        val = cardVal[card[0]]

    return val


cardStack1 = []
cardStack2 = []
tmpStack1 = []
tmpStack2 = []

battle = False
rounds = 0

n = int(raw_input()) # the number of cards for player 1
for i in xrange(n):
    cardp_1 = raw_input() # the n cards of player 1
    cardStack1.append(getCardVal(cardp_1))
m = int(raw_input()) # the number of cards for player 2
for i in xrange(m):
    cardp_2 = raw_input() # the m cards of player 2
    cardStack2.append(getCardVal(cardp_2))

# If none of the card stack is empty
while(len(cardStack1) > 0 and len(cardStack2) > 0):
    # Each one pick a card
    cardPlayer1 = cardStack1.pop(0)
    cardPlayer2 = cardStack2.pop(0)
    # And put it over the temp stack
    tmpStack1.append(cardPlayer1)
    tmpStack2.append(cardPlayer2)

    # We compare the cards
    if(cardPlayer1 > cardPlayer2):
        # We give all the cards to player 1
        cardStack1 += tmpStack1
        cardStack1 += tmpStack2
        del tmpStack1[:]
        del tmpStack2[:]
        rounds += 1
        battle = False
    elif(cardPlayer1 < cardPlayer2):
        # We give all the cards to player 2
        cardStack2 += tmpStack1
        cardStack2 += tmpStack2
        del tmpStack1[:]
        del tmpStack2[:]
        rounds += 1
        battle = False
    else:
        # Equal cars ! I is time to battle !
        battle = True
        nbCardToDiscard1 = 3 if (len(cardStack1) >= 3) else len(cardStack1)
        nbCardToDiscard2 = 3 if (len(cardStack2) >= 3) else len(cardStack2)
        for i in range(0, nbCardToDiscard1):
            tmpStack1.append(cardStack1.pop(0))
        for i in range(0, nbCardToDiscard2):
            tmpStack2.append(cardStack2.pop(0))

# If the game ended during a battle
if(battle):
    print('PAT')
elif(len(cardStack1) > 0):
    print('1 ' + str(rounds))
elif(len(cardStack2) > 0):
    print('2 ' + str(rounds))
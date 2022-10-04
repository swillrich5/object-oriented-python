# HigherOrLower

import enum
import random

# Card Constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard


# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# Main Code
print('Welcome to Higher or Lower.')
print('Choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right awards 20 points.  Getting it wrong deducts 15 point from your score')
print('Your score starts off at 50 points')
print()

startingDeskList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeskList.append(cardDict)

score = 50  # beginning player score

while True:     # Play multiple games
    print()
    gameDeckList = shuffle(startingDeskList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    currentCardValue = currentCardDict['value']
    print(f"Starting card is: { currentCardRank } of { currentCardSuit }")
    print()

    for cardNumber in range(0, NCARDS): # Play one game of this many cards
        answer = input(f"Will the next card be higher or lower than the { currentCardRank } of { currentCardSuit }? (Enter h or l): ")
        answer = answer.casefold()  # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print(f"Next card is { nextCardRank } of { nextCardSuit }")

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You guessed correctly.  It was higher.')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You guessed correctly.  It was lower.')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15
        
        print(f"Your score is: { score }")
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # don't need current suit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK, bye')

                



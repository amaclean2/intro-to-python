import random

def buildDeck() :
    suites = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    deck = []
    for suite in suites :
        for value in values :
            deck.append({
                'value': value,
                'suite': suite,
                'played': False
            })

    return deck

def pullCard() :
    randIdx = random.randrange(0, len(deck) - 1)
    randCard = deck.pop(randIdx)
    return randCard


deck = buildDeck()

print(pullCard())
print(pullCard())
print(pullCard())
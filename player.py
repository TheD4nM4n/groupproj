import deck
import stdio
import random

#Goal: create a 'player' class with a deck.

class Player:

    def __init__(self):
        self.deck = []
    
    def getDeck(self): return self.deck

    def setDeck(self,deck): self.deck = deck

    def drawCard(self): return self.deck.pop(0)

    def __str__(self): return f"Player with a deck of {len(self.deck)} cards."

def compareCards(p1,p2):
    winner = False
    cards = [p1.drawCard(), p2.drawCard()]
    while not winner:
        if cards[-2] > cards[-1]: 
            return [False,cards]
        elif cards[-1] > cards[-2]: 
            return [True,cards]
        else:
            cards.extend(p1.drawCard(), p2.drawCard())

def main(): 

    cards = deck.makeStandardDeck()
    random.shuffle(cards)
    halfIndex = int(len(cards) / 2 )# Not actually sure if this is efficient.

    person, person2 = Player(), Player()

    person.setDeck(cards[:halfIndex])
    person2.setDeck(cards[halfIndex:])

    stdio.writeln(f"person 1: {person}\nperson 2: {person2}")

    stdio.writeln(person.getDeck())
    stdio.writeln(person2.getDeck())

    testRound = compareCards(person,person2)
    stdio.writeln(f"\nTest round: Player {testRound[0]+1} wins. \nCards drawn: {testRound[1]}")

if __name__ == "__main__": main()
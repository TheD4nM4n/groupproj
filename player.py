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

    c1 = person.drawCard()
    c2 = person2.drawCard()

    stdio.writeln(f"{c1} > {c2}: {c1 > c2}")

if __name__ == "__main__": main()
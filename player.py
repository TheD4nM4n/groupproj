import deck
import stdio
import random

#Goal: create a 'player' class with a deck.

class Player:

    def __init__(self):
        self.deck = []
    
    def getDeck(self): return self.deck

    def setDeck(self,deck): self.deck = deck

    def __str__(self): return f"Player with a deck of {len(self.deck)} cards."


def main(): 

    cards = deck.makeStandardDeck()
    random.shuffle(cards)
    halfIndex = len(cards) / 2 # Not actually sure if this is efficient.

    person = Player(cards[:halfIndex])
    person2 = Player(cards[halfIndex:])

    

    stdio.writeln(f"person 1: {person}\nperson 2: {person2}")

    stdio.writeln(person.getDeck())
    stdio.writeln(person2.getDeck())

if __name__ == "__main__": main()
import deck
import stdio

#Goal: create a 'player' class with a deck.

class Player:

    def __init__(self):
        self.deck = []
    
    def getDeck(self): return self.deck

    def setDeck(self,deck): self.deck = deck

    def __str__(self): return f"Player with a deck of {len(self.deck)} cards."


def main(): 

    person = Player()

    person.setDeck(deck.makeStandardDeck())

    stdio.writeln(person)

if __name__ == "__main__": main()
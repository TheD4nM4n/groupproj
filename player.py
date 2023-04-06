import deck

#Goal: create a 'player' class with a deck.

class Player:

    def __init__(self):
        self.deck = deck.makeStandardDeck()
    
    def getDeck(self): return self.deck

    def setDeck(self,deck): self.deck = deck


def main(): return None

if __name__ == "__main__": main()
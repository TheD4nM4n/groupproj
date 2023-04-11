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

def compareCards(p1,p2): #returns an array containing a boolean and then another array of cards.
    cards = [p1.drawCard(), p2.drawCard()]
    while True: #a 'while true' statement is scary, but this one is still definite.
        if cards[-2] > cards[-1]: #cards[-2] is always Player 1's card. cards[-1] is always Player 2's card.
            return [False,cards] #The boolean refers to which player won. False = p1, True = p2.
        elif cards[-1] > cards[-2]: 
            return [True,cards] #Player 2 won + here's the cards
        else:
            if p1.getDeck(): #p1 and p2 have the same deck length. If there are no more cards, this will be false.
                cards.extend([p1.drawCard(), p2.drawCard()]) #Draws one card each and appends it to the list.
            else: return "draw" #Special exception for when the very last card in each deck has the same rank.

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
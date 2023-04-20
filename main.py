import stdio
import stddraw
import constants as c
from picture import Picture
from button import Button
import player
import random
import deck
from card import Card
from graphicalcard import GraphicalCard

p1_score = 0
p2_score = 0

# Initializing all necessary objects
draw_button = Button(640, 360, 90, 45, "WAR!")
player_1, player_2 = player.Player(), player.Player()

p1_card: Card = None
p2_card: Card = None

# Intial setup, only run once

def setup():

    # stddraw tings
    stddraw.setCanvasSize(c.H_RES, c.V_RES)
    stddraw.setXscale(0, 1280)
    stddraw.setYscale(0, 720)

    # creating decks for both players
    cards = deck.makeStandardDeck()
    random.shuffle(cards)
    halfIndex = int(len(cards) / 2 )

    player_1.setDeck(cards[:halfIndex])
    player_2.setDeck(cards[halfIndex:])


def draw_board():

    # Board drawing code, nothing special (thanks keito for the UI idea, and Dipendra for the code :)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(c.P1_BOARD_X, c.P1_BOARD_Y, c.BOARD_W, c.BOARD_H)
    stddraw.filledRectangle(c.P2_BOARD_X, c.P2_BOARD_Y, c.BOARD_W, c.BOARD_H)

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(28)
    stddraw.text(c.P1_TEXT_X, c.P1_TEXT_Y, "Player 1")
    stddraw.text(c.P2_TEXT_X, c.P2_TEXT_Y, "Player 2")

    stddraw.picture(Picture("./cards/Deck1.gif"), c.P1_DECK_X, c.P1_DECK_Y)
    stddraw.picture(Picture("./cards/Deck2.gif"), c.P2_DECK_X, c.P2_DECK_Y)

def draw_score():

    # Score code, draws in each player's board
    stddraw.setFontSize(50)
    stddraw.text(c.P1_SCORE_X, c.P1_SCORE_Y, str(p1_score))
    stddraw.text(c.P2_SCORE_X, c.P2_SCORE_Y, str(p2_score))

def draw_ui():

    # The only functional UI element is the "WAR!" button, so here you go
    stddraw.setFontSize(20)
    draw_button.draw()

if __name__ == "__main__":
    setup()
    while True:

        # Redraw the whole game every time, because pygame
        stddraw.clear(stddraw.DARK_GREEN)
        draw_board()
        draw_score()
        draw_ui()

        # My favorite part, the logic (thanks Josiah for the logic code!)
        if stddraw.mousePressed():
            m_X = stddraw.mouseX()
            m_Y = stddraw.mouseY()
            if draw_button.clicked(m_X, m_Y):
                tied = True
                played_cards = []

                # This continuously draws cards if tied, until one wins
                while tied:
                    p1_card = player_1.drawCard()
                    p2_card = player_2.drawCard()
                    played_cards.extend((p1_card, p2_card))
                    if played_cards[-2] > played_cards[-1]: #cards[-2] is always Player 1's card. cards[-1] is always Player 2's card.
                        tied = False
                        p1_score += len(played_cards)
                    elif played_cards[-1] > played_cards[-2]: 
                        tied = False
                        p2_score += len(played_cards)
                    else:
                        if player_1.getDeck(): #p1 and p2 have the same deck length. If there are no more cards, this will be false.
                            played_cards.extend([player_1.drawCard(), player_2.drawCard()]) #Draws one card each and appends it to the list.
                        else: draw_button.deactivate()
        
        # All I do is win, win, win, no matter what
        if not player_1.getDeck():
            draw_button.deactivate()
            if p1_score > p2_score:
                stddraw.text(640, 72, "Player 1 wins!")
            elif p2_score > p1_score:
                stddraw.text(640, 72, "Player 2 wins!")
            else:
                stddraw.text(640, 72, "It's a draw!")

        # Thanks Prof. Grim for this code, didn't feel like making graphical cards myself
        if isinstance(p1_card, Card):
            GraphicalCard(p1_card.get_rank(), p1_card.get_suit()).draw(640, 180)
            GraphicalCard(p2_card.get_rank(), p2_card.get_suit()).draw(640, 540)
        

        stddraw.show(0)

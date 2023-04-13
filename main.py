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


draw_button = Button(640, 360, 90, 45, "WAR!")
player_1, player_2 = player.Player(), player.Player()

p1_card: Card = None
p2_card: Card = None

def setup():
    stddraw.setCanvasSize(c.H_RES, c.V_RES)
    stddraw.setXscale(0, 1280)
    stddraw.setYscale(0, 720)

    cards = deck.makeStandardDeck()
    random.shuffle(cards)
    halfIndex = int(len(cards) / 2 )

    player_1.setDeck(cards[:halfIndex])
    player_2.setDeck(cards[halfIndex:])


def draw_board():
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
    stddraw.setFontSize(50)
    stddraw.text(c.P1_SCORE_X, c.P1_SCORE_Y, str(p1_score))
    stddraw.text(c.P2_SCORE_X, c.P2_SCORE_Y, str(p2_score))

def draw_ui():
    stddraw.setFontSize(20)
    draw_button.draw()

if __name__ == "__main__":
    setup()
    while True:
        stddraw.clear(stddraw.DARK_GREEN)
        draw_board()
        draw_score()
        draw_ui()

        if stddraw.mousePressed():
            m_X = stddraw.mouseX()
            m_Y = stddraw.mouseY()
            if draw_button.clicked(m_X, m_Y):
                p1_card = player_1.drawCard()
                p2_card = player_2.drawCard()
        
        if isinstance(p1_card, Card):
            GraphicalCard(p1_card.get_rank(), p1_card.get_suit()).draw(640, 180)
            GraphicalCard(p2_card.get_rank(), p2_card.get_suit()).draw(640, 540)
        
        
        stddraw.show(0)

import stdio
import stddraw
import constants as c
from picture import Picture

stddraw.setCanvasSize(c.H_RES, c.V_RES)
stddraw.setXscale(0, 1280)
stddraw.setYscale(0, 720)
stddraw.clear(stddraw.DARK_GREEN)

stddraw.setPenColor(stddraw.WHITE)
stddraw.filledRectangle(c.P1_BOARD_X, c.P1_BOARD_Y, c.BOARD_W, c.BOARD_H)
stddraw.filledRectangle(c.P2_BOARD_X, c.P2_BOARD_Y, c.BOARD_W, c.BOARD_H)

stddraw.setPenColor(stddraw.BLACK)
stddraw.setFontSize(28)
stddraw.text(c.P1_TEXT_X, c.P1_TEXT_Y, "Player 1")
stddraw.text(c.P2_TEXT_X, c.P2_TEXT_Y, "Player 2")

stddraw.setFontSize(50)
stddraw.text(c.P1_SCORE_X, c.P1_SCORE_Y, "0")
stddraw.text(c.P2_SCORE_X, c.P2_SCORE_Y, "0")

stddraw.picture(Picture("./cards/Deck1.gif"), c.P1_DECK_X, c.P1_DECK_Y)
stddraw.picture(Picture("./cards/Deck2.gif"), c.P2_DECK_X, c.P2_DECK_Y)

while True:
    stddraw.show()

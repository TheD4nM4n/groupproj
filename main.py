import stdio
import stddraw
import constants as c

stddraw.setCanvasSize(c.H_RES, c.V_RES)
stddraw.setXscale(0, 1280)
stddraw.setYscale(0, 720)
stddraw.clear(stddraw.DARK_GREEN)

stddraw.setPenColor(stddraw.WHITE)
stddraw.filledRectangle(c.P1_DECK_X, c.P1_DECK_Y, c.DECK_W, c.DECK_H)
stddraw.filledRectangle(c.P2_DECK_X, c.P2_DECK_Y, c.DECK_W, c.DECK_H)

stddraw.setPenColor(stddraw.BLACK)
stddraw.setFontSize(28)
stddraw.text(c.P1_TEXT_X, c.P1_TEXT_Y, "Player 1")
stddraw.text(c.P2_TEXT_X, c.P2_TEXT_Y, "Player 2")
while True:
    stddraw.show()
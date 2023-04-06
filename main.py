import stdio
import stddraw

H_RES = 1280
V_RES = 720

stddraw.setCanvasSize(H_RES, V_RES)
stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)
stddraw.clear(stddraw.DARK_GREEN)

while True:
    stddraw.show()
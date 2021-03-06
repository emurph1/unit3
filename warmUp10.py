#Emily Murphy
#2017-10-06
#warmUp10.py - make wallpaper

from ggame import *

blue = Color(0x0000FF,1)
white = Color(0xFFFFFF,0)

whiteOutline = LineStyle(10, white)

blueRectangle = PolygonAsset([(0,0), (-25, 50), (0,100), (25, 50)], whiteOutline, blue)

for j in range(10):
    for i in range(23):
        Sprite(blueRectangle, (25 + 50*i, 0 + 100*j))

App().run()
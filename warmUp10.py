#Emily Murphy
#2017-10-06
#warmUp10.py - make wallpaper

from ggame import *

blue = Color(0x0000FF,1)
white = Color(0xFFFFFF,0)

whiteOutline = LineStyle(10, white)

blueRectangle = PolygonAsset([(0,0), (-25, 50), (0,100), (25, 50)], whiteOutline, blue)

Sprite(blueRectangle, (25, 0))

App().run()
#Emily Murphy
#2017-10-06
#warmUp10.py - make wallpaper

from ggame import *

blue = Color(0x0000FF,1)
white = Color(0xFFFFFF,0)

whiteOutline = LineStyle(10, white)

blueRectangle = PolygonAsset([(100,0), (20, 100), (300,300), (200, 100)], whiteOutline, blue)

Sprite(blueRectangle, (200, 100))

App().run()
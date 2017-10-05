#Emily Murphy
#2017-10-06
#warmUp10.py - make wallpaper

from ggame import *

blue = Color(0x0000FF,1)
white = Color(0xFFFFFF,0)

whiteOutline = LineStyle(15, white)

blueRectangle = RectangleAsset(500, 200, whiteOutline, blue)


App().run()
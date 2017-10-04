#Emily Murphy
#2017-10-03
#usa.py - use loops to make usa flag

from ggame import *
red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
blue = Color(0x0000FF,1)

whiteOutline = LineStyle(5, white)
redRectangle = RectangleAsset(200, 600, whiteOutline, red)
whiteRectangle = RectangleAsset(500, 200, whiteOutline, white)

i = 0
while i<=7:
    i+=1
    Sprite(i**(redRectangle), (600,200))
    
    
    

App().run()
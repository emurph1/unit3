#Emily Murphy
#2017-10-03
#usa.py - use loops to make usa flag

from ggame import *
red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

whiteOutline = LineStyle(5, white)
blackOutline = LineStyle(1, black)

redRectangle = RectangleAsset(780, 50, whiteOutline, red)
whiteRectangle = RectangleAsset(780, 50, blackOutline, white)

i = 0
while i<=4:
    i+= Sprite(redRectangle, (300,0))
    print(i)
    
i = 0
while i<=3:
    i+=1
    Sprite(whiteRectangle, (300,45))
    
    

App().run()
#Emily Murphy
#2017-10-06
#dotsDemo.py - making dots

from ggame import *

red = Color(0xFF0000, 1)

dot = CircleAsset(20,LineStyle(1,red), red)

for j in range(12): #prints the row 12 times
    for i in range(30): #prints one row of 30 dots
        Sprite(dot, (20 + 40 *i,20 + 50*j))

App().run()

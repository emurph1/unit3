#Emily Murphy
#2017-10-06
#dotsDemo.py - making dots

from ggame import *

red = Color(0xFF0000, 1)

dot = CircleAsset(20,LineStyle(1,red), red)

for j in range(20):
    for i in range(20):
        Sprite(dot, (20 + 40 *i,20))

App().run()

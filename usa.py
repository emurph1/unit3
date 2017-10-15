#Emily Murphy
#2017-10-03
#usa.py - use loops to make usa flag

from ggame import *
#constants
STRIPE_WIDTH=700
STRIPE_HEIGHT=34
STAR_WIDTH=48
STAR_HEIGHT=52
FIRST_STAR_X=10
FIRST_STAR_Y=14
NUM_STRIPES=13
STARS_PER_LONG_ROW=6
STARS_PER_SHORT_ROW=5
NUM_LONG_ROWS=5
NUM_SHORT_ROWS=4
#colors and lines
red = Color(0xFF0000,1)
blue = Color(0x000080,1)
white = Color(0xFFFFFF,1)
redLine = LineStyle(1,red)
blueLine = LineStyle(1,blue)
whiteLine = LineStyle(1,white)
#objects to draw
redStripe = RectangleAsset(STRIPE_WIDTH,STRIPE_HEIGHT,redLine,red)
blueRectangle = RectangleAsset(STRIPE_WIDTH*.4,STRIPE_HEIGHT*7,blueLine,blue)
star = PolygonAsset([(0,0),(8,0),(12,-
8),(16,0),(24,0),(16,4),(18,12),(12,6),(4,12),(8,4)],whiteLine,white)
#Sprite stripes
for i in range(14):
if i%2 == 0:
Sprite(redStripe,(0,i*STRIPE_HEIGHT))
#Sprite blue rectangle
Sprite(blueRectangle)
#Sprite stars
for i in range(NUM_LONG_ROWS):
for j in range(0,STARS_PER_LONG_ROW):
x = FIRST_STAR_X + STAR_WIDTH*j
y = FIRST_STAR_Y + STAR_HEIGHT*i
Sprite(star,(x,y))
for i in range(NUM_SHORT_ROWS):
for j in range(STARS_PER_SHORT_ROW):
x = FIRST_STAR_X + STAR_WIDTH/2 + STAR_WIDTH*j
y = FIRST_STAR_Y + STAR_HEIGHT/2 +STAR_HEIGHT*i
Sprite(star,(x,y))
myApp = App()
myApp.run()

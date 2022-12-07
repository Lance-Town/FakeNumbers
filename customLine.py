# Possible temporary file that I did some testing with my own custom line function instead of the built in 
# ImageDraw.line(). Not sure what to do with the code so I just put it here in case I need it again.

from PIL import Image, ImageDraw
import random as rd
import plotAlgo as pa

# draws a one in middle of screen
def drawOne(draw: ImageDraw, image: Image, size):
    # Get the start and end points of the base of the one
    baseStartX = int(size[0]/2) + rd.randint(-2,1)
    baseStartY = rd.randint(3,10)
    baseEndX = int(size[0]/2) + rd.randint(-2,1)
    baseEndY = size[1] - rd.randint(0,10)

    # Get the coordinates for the little head at the top of the one
    pointY = rd.randint(-1, 3)
    if pointY == -1:
        headEndX = baseStartX - rd.randint(1,2)
    elif pointY == 3:
        headEndX = baseStartX - rd.randint(2,3)
    else:
        headEndX = baseStartX - rd.randint(1,3)

    headEndY = baseStartY + pointY

    # Get the coordinates for the little tail at the end of the one
    pointY = rd.randint(-3,3)
    if pointY > 1 or pointY < -1:
        pointX = rd.randint(2,3)
    else:
        pointX = rd.randint(1,3)
    tailStartX = baseEndX - pointX
    tailStartY = baseEndY + pointY

    tailEndX = baseEndX + pointX
    tailEndY =  baseEndY - pointY

    # Draw the base one line
    pa.drawLine(draw=draw, coordOne=(baseStartX, baseStartY), coordTwo=(baseEndX, baseEndY))

    # draw the base tail
    pa.drawLine(draw=draw, coordOne=(tailStartX, tailStartY), coordTwo=(tailEndX, tailEndY))

    # draw base head
    pa.drawLine(draw=draw, coordOne=(headEndX, headEndY), coordTwo=(baseStartX, baseStartY))
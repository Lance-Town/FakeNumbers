from PIL import Image, ImageDraw
import numpy as np
import random as rd
import customLine as cl
import math

#TODO Make the line drawing antialiased or something to make to look like a real pencil line

# This is a custom line that will be able to draw a line with each pixel being a different color
def testLine(draw: ImageDraw, image: Image, size):
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


    # Not super sure but this all just doesn't work
    # draw the first base line
    cl.drawLine(draw=draw, coordOne=(baseStartY, baseStartX), coordTwo=(baseEndY, baseEndX))

    # draw the first head line

    # draw the first tail line
    cl.drawLine(draw=draw, coordOne=(tailStartX, tailStartY), coordTwo=(tailEndX, tailEndY))

def main():
    # The format and size of the file
    FORMAT = 'RGB'
    SIZE = (15,40)
    BACKGROUND = (250 + rd.randint(-5,5), 250 + rd.randint(-5,5), 250 + rd.randint(-5,5))

    # create a new image
    image = Image.new(FORMAT, SIZE, BACKGROUND)

    # Draw on the new image
    draw = ImageDraw.Draw(image)

    cl.drawOne(draw,image, image.size)

    image.show()


if __name__ == '__main__': 
    main()
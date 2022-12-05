from PIL import Image, ImageDraw
import numpy as np
import random as rd

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

    # Draw the faintest third line that surrounds the base and head
    grayOne = rd.randint(10,33)
    grayTwo = rd.randint(10,33)
    draw.line(((headEndX+2, headEndY+2), (baseStartX+2, baseStartY), (baseEndX+2, baseEndY)), fill=(grayOne,grayOne,grayOne,rd.randint(240,255)), width=1)
    draw.line(((headEndX+2, headEndY-2), (baseStartX-2, baseStartY), (baseEndX-2, baseEndY)), fill=(grayTwo,grayTwo,grayTwo,rd.randint(240,255)), width=1)
    
    # Draw the faintest third line that surrounds the tail
    grayOne = rd.randint(10,33)
    grayTwo = rd.randint(10,33)
    draw.line(((tailStartX+2, tailStartY), (tailEndX+2, tailEndY)), fill=(grayOne,grayOne,grayOne,rd.randint(100,200)), width = 1)
    draw.line(((tailStartX-2, tailStartY), (tailEndX-2, tailEndY+1)), fill=(grayTwo,grayTwo,grayTwo,rd.randint(100,200)), width = 1)

    # Draw the faint second line that surrounds the base and head
    grayOne = rd.randint(55,99)
    grayTwo = rd.randint(55,99)
    draw.line(((headEndX+1, headEndY+1), (baseStartX+1, baseStartY), (baseEndX+1, baseEndY)), fill=(grayOne,grayOne,grayOne,rd.randint(100,200)), width=1)
    draw.line(((headEndX+1, headEndY-1), (baseStartX-1, baseStartY), (baseEndX-1, baseEndY)), fill=(grayTwo,grayTwo,grayTwo,rd.randint(100,200)), width=1)

    # Draw the faint second line that surrounds the tail
    grayOne = rd.randint(55,99)
    grayTwo = rd.randint(55,99)
    draw.line(((tailStartX+1, tailStartY), (tailEndX+1, tailEndY)), fill=(grayOne,grayOne,grayOne,rd.randint(100,200)), width = 1)
    draw.line(((tailStartX-1, tailStartY), (tailEndX-1, tailEndY)), fill=(grayTwo,grayTwo,grayTwo,rd.randint(100,200)), width = 1)

    # Draw the base one line
    draw.line(((headEndX, headEndY), (baseStartX, baseStartY), (baseEndX, baseEndY)), fill=(255,255,255,255), width=1)

    # Draw the tail of the one
    draw.line(((tailStartX, tailStartY), (tailEndX, tailEndY)), fill=(255,255,255,255), width = 1)


def main():
    # The format and size of the file
    FORMAT = 'RGBA'
    SIZE = (15,30)

    # create a new image
    image = Image.new(FORMAT, SIZE, (0,0,0,255))

    # Draw on the new image
    draw = ImageDraw.Draw(image)

    drawOne(draw,image, image.size)
    image.show()


if __name__ == '__main__': 
    main()
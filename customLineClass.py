from PIL import Image, ImageDraw
import random as rd
import numpy as np
from scipy.interpolate import BPoly
import math

# Custom class to hold the image
class CImage: 
    # Format, size and background of file
    FORMAT = 'RGB'
    SIZE = (15,40)
    BACKGROUND = (250 + rd.randint(-5,5), 250 + rd.randint(-5,5), 250 + rd.randint(-5,5))

    image = Image.new(FORMAT, SIZE, BACKGROUND)
    draw = ImageDraw.Draw(image)

    def __init__(self) -> Image:
        pass
    
    def drawLine(self, coordOne, coordTwo, color):
        x0, y0 = coordOne
        x1, y1 = coordTwo

        # Set x and y to starting positions
        y = y0
        x = x0

        # get difference between start and end points
        dx = x1 - x0
        dy = y1 - y0

        # Get distance between points
        dxy = math.sqrt((dx**2 + dy**2))

        # difference to be added to x and y at each interval
        dx /= dxy
        dy /= dxy

        # loop through line and plot points
        for _ in range(int(dxy)):
            pxlColorShift = color + rd.randint(-10,10)
            self.draw.point((round(x),round(y)), fill=(pxlColorShift, pxlColorShift, pxlColorShift))
            x += dx
            y += dy

    def drawOne(self):
        # Get the start and end points of the base of the one
        baseStartX = int(self.image.size[0]/2) + rd.randint(-2,1)
        baseStartY = rd.randint(3,10)
        baseEndX = int(self.image.size[0]/2) + rd.randint(-2,1)
        baseEndY = self.image.size[1] - rd.randint(4,10)

        # Get the coordinates for the little head at the top of the one
        pointY = rd.randint(-1, 3)
        if pointY == -1:
            headEndX = baseStartX - rd.randint(2,4)
        elif pointY == 3:
            headEndX = baseStartX - rd.randint(3,5)
        else:
            headEndX = baseStartX - rd.randint(2,5)

        headEndY = baseStartY + pointY

        # Get the coordinates for the little tail at the end of the one
        pointY = rd.randint(-3,3)
        if pointY > 1 or pointY < -1:
            pointX = rd.randint(3,5)
        else:
            pointX = rd.randint(2,5)
        tailStartX = baseEndX - pointX
        tailStartY = baseEndY + pointY

        tailEndX = baseEndX + pointX
        tailEndY =  baseEndY - pointY

        # draw faint base lines
        self.drawLine(coordOne=(baseStartX+2, baseStartY), coordTwo=(baseEndX+2, baseEndY), color=rd.randint(200,240))
        self.drawLine(coordOne=(baseStartX-1, baseStartY), coordTwo=(baseEndX-1, baseEndY), color=rd.randint(200,240))

        # draw faint tail lines
        self.drawLine(coordOne=(tailStartX+2, tailStartY), coordTwo=(tailEndX+2, tailEndY), color=rd.randint(200,240))
        self.drawLine(coordOne=(tailStartX-1, tailStartY), coordTwo=(tailEndX-1, tailEndY), color=rd.randint(200,240))

        # draw faint head lines
        self.drawLine(coordOne=(headEndX-1, headEndY), coordTwo=(baseStartX-1, baseStartY), color=rd.randint(200,240))
        self.drawLine(coordOne=(headEndX+2, headEndY), coordTwo=(baseStartX+2, baseStartY), color=rd.randint(200,240))

        # draw base head
        self.drawLine(coordOne=(headEndX, headEndY), coordTwo=(baseStartX, baseStartY), color=rd.randint(120,150))
        self.drawLine(coordOne=(headEndX+1, headEndY), coordTwo=(baseStartX+1, baseStartY), color=rd.randint(120,150))

        # draw the base tail
        self.drawLine(coordOne=(tailStartX, tailStartY), coordTwo=(tailEndX, tailEndY), color=rd.randint(120,150))
        self.drawLine(coordOne=(tailStartX+1, tailStartY), coordTwo=(tailEndX+1, tailEndY), color=rd.randint(120,150))

        # draw the base one line
        self.drawLine(coordOne=(baseStartX, baseStartY), coordTwo=(baseEndX, baseEndY), color=rd.randint(120,150))
        self.drawLine(coordOne=(baseStartX+1, baseStartY), coordTwo=(baseEndX+1, baseEndY), color=rd.randint(120,150))

    # draw the number two
    def drawTwo(self):
        # get points for base number two
        # FIXME adjust the points to not allow the two to go off the image
        startPoint = (rd.randint(1,5), rd.randint(1,3))
        middlePointOne = (self.image.size[0] + rd.randint(5,10), rd.randint(-12, 5))
        jointPoint = (rd.randint(2,7), self.image.size[1] - rd.randint(3,10))
        lastPoint = (self.image.size[0] - rd.randint(1,5), self.image.size[1] - rd.randint(0,10))

        # draw lines
        self.bezier((startPoint, middlePointOne, jointPoint), 144, 2)
        self.drawLine(coordOne=jointPoint, coordTwo=lastPoint, color=144)
        self.drawLine(coordOne=(jointPoint[0]-1, jointPoint[1]), coordTwo=lastPoint, color=144)
    
    def show(self):
        self.image.show()
    
    # still testing for bezier
    def bezier(self, coords, color, width=1):
        width = width if width>0 else 0

        cp = np.array([tup for tup in coords])
        curve = BPoly(cp[:, None, :], [0, 1])

        # FIXME change it to use the minimum needed points on the line instead of arbitrary 100 points
        x = np.linspace(0, 1, 100)

        points = curve(x)

        # plot lines
        for x, y in points:
            pxlColorShift = color + rd.randint(-10,10)
            faintColorShift = color + rd.randint(50,90)

            for wid in range(width):
                # base lines
                self.draw.point((x-wid+1, y), fill=(pxlColorShift,pxlColorShift,pxlColorShift))
                
                # faint lines
                self.draw.point((x-wid, y), fill=(faintColorShift, faintColorShift, faintColorShift))
                self.draw.point((x+1, y), fill=(faintColorShift, faintColorShift, faintColorShift))
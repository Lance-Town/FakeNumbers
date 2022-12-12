from PIL import Image, ImageDraw
import random as rd
import numpy as np
from scipy.interpolate import BPoly
import math

# Custom class to hold the image
class CImage: 
    # Format, size and background of file
    FORMAT = 'RGB'
    SIZE = (8,8)
    BACKGROUND = (250 + rd.randint(-5,5), 250 + rd.randint(-5,5), 250 + rd.randint(-5,5))

    def __init__(self) -> Image:
        self.image = Image.new(self.FORMAT, self.SIZE, self.BACKGROUND)
        self.draw = ImageDraw.Draw(self.image)

    def getGradient(self):
        return rd.randint(7_000, 15_000) / 10_000

    def show(self):
        self.image.show()
    
    # still testing for bezier
    def bezier(self, coords, color, gradient, width=1):
        width = width if width>0 else 0

        # coordinate points
        cp = np.array([tup for tup in coords])
        curve = BPoly(cp[:, None, :], [0, 1])

        # FIXME change it to use the minimum needed points on the line instead of arbitrary 100 points
        x = np.linspace(0, 1, 100)

        grad = np.linspace(1, gradient, 100)
        points = curve(x)

        # plot lines
        i = 0
        for x, y in points:
            pxlColorShift = int((color + rd.randint(-30,30)) * grad[i])
            faintColorShift = int((color + rd.randint(20,50)) * grad[i])

            i+=1
            for wid in range(width):
                # faint lines
                self.draw.point((x-wid, y), fill=(faintColorShift, faintColorShift, faintColorShift))
                self.draw.point((x+1, y), fill=(faintColorShift, faintColorShift, faintColorShift))

                # base lines
                self.draw.point((x-wid+1, y), fill=(pxlColorShift,pxlColorShift,pxlColorShift))
    
    def drawLine(self, coordOne, coordTwo, color, gradient=1):
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

        grad = np.linspace(1, gradient, int(dxy))

        # difference to be added to x and y at each interval
        dx /= dxy
        dy /= dxy

        # loop through line and plot points
        for i in range(int(dxy)):
            pxlColorShift = int((color + rd.randint(-30,30)) * grad[i])
            self.draw.point((round(x),round(y)), fill=(pxlColorShift, pxlColorShift, pxlColorShift))
            x += dx
            y += dy

    def drawOne(self):
        gradient = self.getGradient()

        # Get the start and end points of the base of the one
        x = self.image.size[0]
        y = self.image.size[1]
        baseStartX = int(x/2) + round(x * (rd.randint(-14, 7)/100))
        baseStartY = int((rd.randint(7,25)/100)*y)
        baseEndX = int(x/2) + round(x * (rd.randint(-14, 7)/100))
        baseEndY = y - int(y * (rd.randint(10,25)/100))

        # Get the coordinates for the little head at the top of the one
        pointY = (rd.randint(-2, 8)/100)
        # if pointY < 0:
        #     headEndX = int(baseStartX - x*(rd.randint(13,26)/100))
        # elif pointY < 0.03:
        #     headEndX = int(baseStartX - x*(rd.randint(20,33)/100))
        # else:
        #     headEndX = int(baseStartX - x*(rd.randint(13,33)/100))
        headEndX = int(baseStartX - x*(rd.randint(13,33)/100))
        headEndY = int(baseStartY + y*(pointY))

        # Get the coordinates for the little tail at the end of the one
        pointY = rd.randint(-7,7)/100
        if pointY > 0.02 or pointY < -0.02:
            pointX = rd.randint(20,33)/100
        else:
            pointX = rd.randint(13,33)/100
        # tailStartX = baseEndX - (x * pointX)
        # tailStartY = baseEndY + (y * pointY)

        # tailEndX = baseEndX + (x * pointX)
        # tailEndY =  baseEndY - (y * pointY)

        baseColor = rd.randint(40,160)

        # draw faint base lines
        self.drawLine(coordOne=(baseStartX+2, baseStartY), coordTwo=(baseEndX+2, baseEndY), color=baseColor+rd.randint(20,90))
        self.drawLine(coordOne=(baseStartX-1, baseStartY), coordTwo=(baseEndX-1, baseEndY), color=baseColor+rd.randint(40,90))

        # possibly temporarily removing tail from testing
        # draw faint tail lines
        # self.drawLine(coordOne=(tailStartX+2, tailStartY), coordTwo=(tailEndX+2, tailEndY), color=baseColor+rd.randint(40,90))
        # self.drawLine(coordOne=(tailStartX-1, tailStartY), coordTwo=(tailEndX-1, tailEndY), color=baseColor+rd.randint(40,90))

        # draw faint head lines
        self.drawLine(coordOne=(headEndX-1, headEndY), coordTwo=(baseStartX-1, baseStartY), color=baseColor+rd.randint(40,90))
        self.drawLine(coordOne=(headEndX+2, headEndY), coordTwo=(baseStartX+2, baseStartY), color=baseColor+rd.randint(40,90))

        # draw base head
        self.drawLine(coordOne=(headEndX, headEndY), coordTwo=(baseStartX, baseStartY), color=baseColor+rd.randint(-30,30), gradient=gradient)
        self.drawLine(coordOne=(headEndX+1, headEndY), coordTwo=(baseStartX+1, baseStartY), color=baseColor+rd.randint(-30,30), gradient=gradient)

        # possibly temporarily removing tail from testing
        # draw the base tail
        # self.drawLine(coordOne=(tailStartX, tailStartY), coordTwo=(tailEndX, tailEndY), color=baseColor+rd.randint(-30,30), gradient=gradient)
        # self.drawLine(coordOne=(tailStartX+1, tailStartY), coordTwo=(tailEndX+1, tailEndY), color=baseColor+rd.randint(-30,30), gradient=gradient)

        # draw the base one line
        self.drawLine(coordOne=(baseStartX, baseStartY), coordTwo=(baseEndX, baseEndY), color=baseColor+rd.randint(-30,30), gradient=gradient)
        self.drawLine(coordOne=(baseStartX+1, baseStartY), coordTwo=(baseEndX+1, baseEndY), color=baseColor+rd.randint(-30,30), gradient=gradient)

    # draw the number two
    def drawTwo(self):
        gradient = self.getGradient()
        x = self.image.size[0]
        y = self.image.size[1]

        # get points for base number two
        px = int(x*(rd.randint(13,26)/100))
        py = int(y*(rd.randint(7, 13)/100))
        startPoint = (px, py)

        px = x + int(x*(rd.randint(0, 46)/100))
        py = int(y * (rd.randint(-18, 10)/100))
        middlePointOne = (px, py)

        px = int(x*(rd.randint(13, 40)/100))
        py = y - int(y*(rd.randint(7, 25)/100))
        jointPoint = (px, py)

        px = jointPoint[0] + round(x*(rd.randint(45, 70)/100))
        py = y - int(y*(rd.randint(5, 25)/100))
        lastPoint = (px, py)

        bezColor = rd.randint(40,140)
        faintColor = (bezColor*gradient) + rd.randint(-30,30)
        
        # draw faint lines
        self.drawLine(coordOne=(jointPoint[0], jointPoint[1]+1), coordTwo=(lastPoint[0], lastPoint[1]+1), color=faintColor+rd.randint(10,40))
        self.drawLine(coordOne=(jointPoint[0], jointPoint[1]-1), coordTwo=(lastPoint[0], lastPoint[1]-1), color=faintColor+rd.randint(10,40))

        # draw lines
        self.bezier((startPoint, middlePointOne, jointPoint), color=bezColor, gradient=gradient)
        self.drawLine(coordOne=jointPoint, coordTwo=lastPoint, color=faintColor, gradient=gradient)
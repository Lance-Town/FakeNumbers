from PIL import Image, ImageDraw
import random as rd
import math

# Custom class to hold the image
class cImage: 
    # Format, size and background of file
    FORMAT = 'RGB'
    SIZE = (15,30)
    BACKGROUND = (250 + rd.randint(-5,5), 250 + rd.randint(-5,5), 250 + rd.randint(-5,5))

    image = Image.new(FORMAT, SIZE, BACKGROUND)
    draw = ImageDraw.Draw(image)

    def __init__(self) -> Image:
        pass
    
    def drawLine(self, coordOne, coordTwo):
        x0 = coordOne[0]
        y0 = coordOne[1]
        x1 = coordTwo[0]
        y1 = coordTwo[1]

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
            self.draw.point((round(x),round(y)), (0, 0, 0))
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
        self.drawLine(coordOne=(baseStartX, baseStartY), coordTwo=(baseEndX, baseEndY))
        # draw the base tail
        self.drawLine(coordOne=(tailStartX, tailStartY), coordTwo=(tailEndX, tailEndY))

        # draw base head
        self.drawLine(coordOne=(headEndX, headEndY), coordTwo=(baseStartX, baseStartY))
    
    def show(self):
        self.image.show()
        
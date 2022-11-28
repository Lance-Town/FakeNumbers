from PIL import Image, ImageDraw
import random as rd

def drawOne(draw: ImageDraw, size):
    # Get the start and end points of the base of the one
    baseStartX = int(size[0]/2) + rd.randint(-3,3)
    baseStartY = rd.randint(3,10)
    baseEndX = int(size[0]/2) + rd.randint(-3,3)
    baseEndY = size[1] - rd.randint(0,10)

    # Get the coordinates for the little head at the top of the one
    headEndX = baseStartX - rd.randint(1,3)
    headEndY = baseStartY + rd.randint(-1, 3)

    # Get the coordinates for the little tail at the end of the one
    pointX = rd.randint(1,3)
    pointY = rd.randint(1,3)
    tailStartX = baseEndX - pointX
    tailStartY = baseEndY - pointY
    tailEndX = baseEndX + pointX
    tailEndY =  baseEndY + pointY

    # Draw the base one line
    draw.line(((baseStartX, baseStartY), (baseEndX, baseEndY)), fill=(255,255,255), width=1)

    # Draw the head of the one
    draw.line(((baseStartX, baseStartY), (headEndX, headEndY)), fill=(255,255,255), width = 1)

    # Draw the tail of the one
    draw.line(((tailStartX, tailStartY), (tailEndX, tailEndY)), fill=(255,255,255), width = 1)


def main():
    # The format and size of the file
    FORMAT = 'RGB'
    SIZE = (28,28)

    # create a new image
    image = Image.new(FORMAT, SIZE)

    # Draw on the new image
    draw = ImageDraw.Draw(image)

    drawOne(draw, image.size)
    image.show()

if __name__ == '__main__': 
    main()
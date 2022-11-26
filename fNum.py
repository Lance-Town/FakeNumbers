from PIL import Image, ImageDraw
import random as rd

def drawOne(draw: ImageDraw, size):
    # Get the start and end points of the base of the one
    baseStartX = int(size[0]/2)
    baseStartY = rd.randint(3,10)
    baseEndX = int(size[0]/2)
    baseEndY = size[1] - rd.randint(0,10)

    # Get the coordinates for the little head at the top of the one
    headEndX = baseStartX - rd.randint(0,3)
    headEndY = baseStartY + rd.randint(-3, 3)

    # Draw the base one line
    draw.line(((baseStartX, baseStartY), (baseEndX, baseEndY)), width=1)

    # Draw the head of the one
    draw.line(((baseStartX, baseStartY), (headEndX, headEndY)), width = 1)


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
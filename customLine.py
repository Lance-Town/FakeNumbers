# Possible temporary file that I did some testing with my own custom line function instead of the built in 
# ImageDraw.line(). Not sure what to do with the code so I just put it here in case I need it again.

# Gets the slope from the two points
def getSlope(coordOne, coordTwo):
    top = coordTwo[1] - coordOne[1]
    bot = coordTwo[0] - coordOne[0]

    # division by zero
    if bot == 0:
        return 1

    return(top/bot)

# Gets the x variable in the x=(y-b)/m equation
def getX(y: int, m, b):
    return(int((y - b)/m))

# Draws a line from two coordinates 
def drawLine(image: Image, coordOne, coordTwo):
    startX = coordOne[0]
    startY = coordOne[1]
    endY = coordTwo[1]

    m = getSlope(coordOne, coordTwo)
    b = startY - (m*startX)

    pix = image.load()

    for y in range(startY, endY+1):
        x = getX(y=y, m=m, b=b)
        pix[x,y] = (255,255,255,255)
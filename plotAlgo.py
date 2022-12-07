from PIL import Image, ImageDraw
import random as rd
import math

''' Xiaolin Wu's Antialiasing line algo '''
# Integer part of x
def ipart(x):
    return math.floor(x)

def customRound(x):
    return ipart(x+0.5)

# Fractional part of x
def fpart(x):
    return (x - ipart(x)) if x > 0 else (x-(ipart(x)+1))

def rfpart(x):
    return (1-fpart(x))

def plot(draw: ImageDraw, x, y, a):
    draw.point((x, y), (int(a), int(a), int(a)))

def drawAALine(draw: ImageDraw, coordOne, coordTwo):
    x0 = coordOne[0]
    y0 = coordOne[1]
    x1 = coordTwo[0]
    y1 = coordTwo[1]

    steep = abs(y1-y0) > abs(x1 - x0)

    if steep:
        # Swap x0 and y0
        x0, y0 = y0, x0

        # swap x1 and y1
        x1, y1 = y1, x1
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    if dx == 0.0:
        gradient = 1.0
    else:
        gradient = dy / dx

    # first endpoint
    xend = customRound(x0)
    yend = y0 + gradient * (xend - x0)
    xgap = rfpart(x0 + 0.5)
    xpxl1 = xend
    ypxl1 = ipart(yend)
    if steep:
        plot(draw, ypxl1,   xpxl1, rfpart(yend) * xgap)
        plot(draw, ypxl1+1, xpxl1,  fpart(yend) * xgap)
    else:
        plot(draw, xpxl1, ypxl1, rfpart(yend) * xgap)
        plot(draw, xpxl1, ypxl1+1,  fpart(yend) * xgap)
    # intery is first y-intersection for main loop
    intery = yend + gradient

    # second endpoint
    xend = customRound(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = fpart(x1 + 0.5)
    xpxl2 = xend
    ypxl2 = ipart(yend)

    if steep:
        plot(draw, ypxl2, xpxl2, rfpart(yend) * xgap)
        plot(draw, ypxl2+1, xpxl2,  fpart(yend) * xgap)
    else:
        plot(draw, xpxl2, ypxl2,  rfpart(yend) * xgap)
        plot(draw, xpxl2, ypxl2+1, fpart(yend) * xgap)

    # main loop
    if steep:
        for x in range(xpxl1+1, xpxl2):
            plot(draw, ipart(intery), x, rfpart(intery))
            plot(draw, ipart(intery)+1, x,  fpart(intery))
            intery = intery + gradient
    else:
        for x in range(xpxl1+1, xpxl2):
            plot(draw, x, ipart(intery),  rfpart(intery))
            plot(draw, x, ipart(intery)+1, fpart(intery))
            intery = intery + gradient

'''Bresenham's Line Generation -- won't work'''
def bresenham(draw: ImageDraw, coordOne, coordTwo):
    x1 = coordOne[0]
    y1 = coordOne[1]
    x2 = coordTwo[0]
    y2 = coordTwo[1]

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    pk = 2 * dy - dx

    for i in range(0, dx+1):
        if (x1 < x2):
            x1 = x1 + 1
        else:
            x1 = x1 - 1

        if (pk < 0):
            plot(draw=draw, x=x1, y=y1, a=255)
            pk = pk + 2 * dy
        else:
            if (y1 < y2):
                y1 = y1 + 1
            else:
                y1 = y1 - 1

            plot(draw=draw, x=x1, y=y1, a=255)
            pk = pk + 2 * dy - 2 * dx


''' Personal custom line -- modified DDA '''
def drawLine(draw: ImageDraw, coordOne, coordTwo):
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
    dxy = math.sqrt((pow(dx, 2) + pow(dy, 2)))

    # difference to be added to x and y at each interval
    dx /= dxy
    dy /= dxy

    # loop through line and plot points
    for i in range(int(dxy)):
        draw.point((round(x),round(y)), (0, 0, 0))
        x += dx
        y += dy
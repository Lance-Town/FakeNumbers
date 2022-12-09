import customLineClass as custom

#TODO Make the line drawing antialiased or something to make to look like a real pencil line

def main():
    # create a new image
    image = custom.CImage()

    # Draw on the new image
    image.drawOne()

    image.show()


if __name__ == '__main__': 
    main()
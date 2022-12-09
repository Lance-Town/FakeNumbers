import customLineClass as custom

def main():
    # create a new image
    image = custom.CImage()

    # Draw on the new image
    image.bezier((2,2), (15,0), (13,30))

    image.show()


if __name__ == '__main__': 
    main()
import base64

import numpy as np

from ImageTiling import *
from RGBHexUtils import *


def saveStringToFile(outputString):
    file = open("output.txt", "w")
    file.write(outputString)
    file.close()


def encodeImageToBase64(img):
    jpg_img = cv2.imencode('.bmp', img)
    #print(len(jpg_img[1]))
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    return b64_string

def encodeRGBImgToRGB565Hex(img):
    rgb565Bitmap = ""
    for x in range(0, len(img[0])):
        for y in range(0, len(img)):
            rgb565 = convert888To565(img[y][x])
            rgb565Bitmap += "{0:04x}".format(int(rgb565))

    return rgb565Bitmap


def createGcodeWithEmbeddedThumbnailFromTile(tile):
    # Open and Header
    gcodeFile = open("Wallpaper/Wallpaper{:d}X{:d}Y.gcode".format(tile[0], tile[1]), "w")

    # Encode And Write Thumbnail
    img = cv2.imread("Tiles/{:d}x{:d}y.jpg".format(tile[0], tile[1]))
    rgb565Image = encodeRGBImgToRGB565Hex(img)

    gcodeFile.write(";\n; thumbnail begin 40x24 {}\n; ".format(len(rgb565Image)))
    for i in range(0, len(rgb565Image)):
        gcodeFile.write(rgb565Image[i])
        if i % 70 == 0 and i != 0:
            gcodeFile.write("\n; ")
    gcodeFile.write("\n; thumbnail end\n;")

    # Close to Save
    gcodeFile.close()


def createGcodes(imageTiles):
    for tile in imageTiles:
        createGcodeWithEmbeddedThumbnailFromTile(tile)


# PROGRAM
baseImage = LoadImage("Images/TestGreen.png")
imageTiles = SplitImageIntoTiles(baseImage)
createGcodes(imageTiles)


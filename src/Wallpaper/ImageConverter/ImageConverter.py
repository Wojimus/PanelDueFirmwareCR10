import base64

from ImageTiling import *
from RGBHexUtils import *
from Compression import *


def encodeImageToBase64(img):
    jpg_img = cv2.imencode('.bmp', img)
    # print(len(jpg_img[1]))
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    return b64_string


def encodeRGBImgToRGB565Hex(img):
    print("Encoding Image To RGB565 Hex")
    rgb565Bitmap = ""
    for x in range(0, len(img[0])):
        for y in range(0, len(img)):
            rgb565 = convert888To565(img[y][x])
            rgb565Bitmap += "{0:04x}".format(int(rgb565))

    return rgb565Bitmap


def createGcodeWithEmbeddedThumbnailFromImage(img, filename, compress=False, multiplierBitAmount=2):
    # Open and Header
    gcodeFile = open(filename, "w")

    # Convert Image To RGB 565 HEX
    hexString = encodeRGBImgToRGB565Hex(img)

    if compress:
        hexString = RLECompressHexString(hexString, 4, multiplierBitAmount)

    print("Writing Thumbnail GCode")
    # Header (Data Begin Offset : Width : Height: Data Length : Multiplier Bit Length)
    dataOffset = (8 * 5) + (3 * 5) + 3  # 4x 8 Long Hex, 5x 3 Character Seperator, \n;
    Header = ";" + "{0:08x}".format(dataOffset) + "===" \
             + "{0:08x}".format(len(img[0])) + "===" \
             + "{0:08x}".format(len(img)) + "===" \
             + "{0:08x}".format(len(hexString)) + "===" \
             + "{0:08x}".format(multiplierBitAmount) + "===\n;"
    gcodeFile.write(Header)

    # Body
    for i in range(0, len(hexString)):
        gcodeFile.write(hexString[i])
        if (i + 1) % 64 == 0 and i != 0:
            gcodeFile.write("\n;")

    # Close to Save
    gcodeFile.close()


def createGcodeWithEmbeddedThumbnailFromTile(tile):
    # Open and Header
    filename = "Wallpaper/Wallpaper{:d}X{:d}Y.gcode".format(tile[0], tile[1])

    # Encode And Write Thumbnail
    img = cv2.imread("Tiles/{:d}x{:d}y.jpg".format(tile[0], tile[1]))
    createGcodeWithEmbeddedThumbnailFromImage(img, filename)


def createTileGcodes(imageTiles):
    for tile in imageTiles:
        createGcodeWithEmbeddedThumbnailFromTile(tile)


# PROGRAM
baseImage = LoadImage("Images/TestGreen.png")
createGcodeWithEmbeddedThumbnailFromImage(baseImage, "Wallpaper/Wallpaper.gcode", compress=False, multiplierBitAmount=2)
# imageTiles = SplitImageIntoTiles(baseImage)
# createTileGcodes(imageTiles)

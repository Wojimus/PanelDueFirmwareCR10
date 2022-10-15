import base64
from RGBHexUtils import *

def ProcessImageTo16BitHexArray(img):
    hex565Array = []
    for y in range(0, img.shape[0]):
        row = []
        for x in range(0, img.shape[1]):
            rgb888 = img[y][x]
            rgb565 = convert888To565(rgb888)
            row.append(rgb565ToHex(rgb565))
        hex565Array.append(row)

    return hex565Array


def ProcessImageTo16BitHexArraySplitInto100Blocks(img):
    blocks = []
    for i in range(0, 10):
        for j in range(0, 10):
            hex565Array = []
            for y in range(48 * i, 48 * (i + 1)):
                row = []
                for x in range(80 * j, 80 * (j + 1)):
                    rgb888 = img[y][x]
                    rgb565 = convert888To565(rgb888)
                    row.append(rgb565ToHex(rgb565))
                hex565Array.append(row)

            blocks.append(hex565Array)
    print(len(blocks))
    return blocks


def Process16BitHexArrayToBase64String(hexArray):
    # Flatten Array
    flattenedArray = ""
    for x in range(0, len(hexArray)):
        for y in range(0, len(hexArray[0])):
            flattenedArray += base64.b64encode(hexArray[x][y].encode())


def hexArrayToC2DArray(hexArray):
    height = len(hexArray)
    width = len(hexArray[0])
    output = "uint16_t hexArray[{}][{}] = {}".format(width, height, "{")
    for x in range(0, width):
        output += "{"
        for y in range(0, height):
            output += hexArray[y][x]
            if y != height - 1:
                output += ", "
        if x != width - 1:
            output += "}, "
    output += "}};"
    return output
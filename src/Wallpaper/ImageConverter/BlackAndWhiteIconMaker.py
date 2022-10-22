import cv2


def loadIconAndResize(iconPath):
    icon = cv2.imread(iconPath, 0)
    icon = cv2.resize(icon, (70, 70), interpolation=cv2.INTER_AREA)
    return icon


def iconToCharArray(icon):
    charArray = []
    for y in range(0, len(icon)):
        row = []
        for x in range(0, len(icon[0])):
            value = icon[y][x]
            if value >= GRAYSCALE_THRESHOLD:
                row.append(1)
            else:
                row.append(0)
        charArray.append(row)
    return charArray


def generateCU8IntArray(charArray):
    # Open File
    fileHandle = open("GeneratedIcons/{}.txt".format(TARGET_FILE), "w")

    # Write Start
    fileHandle.write("extern const uint8_t " + TARGET_FILE + "Icon[] = \n{ " + str(len(charArray[0])) + ", " + str(len(charArray)) + ",\n")

    # Write body
    for y in range(0, len(charArray)):
        for x in range(0, len(charArray[0])):
            fileHandle.write("0x{0:02x}, ".format(charArray[y][x]))
            if x == len(charArray[0]) - 1:
                fileHandle.write("\n")
    fileHandle.write("};")

    # Close File
    fileHandle.close()

    return


# Program Settings
TARGET_FILE = "Home"
TARGET_SIZE = 70  # px
GRAYSCALE_THRESHOLD = 100  # 0-255


icon = loadIconAndResize("IconSrc/{}.png".format(TARGET_FILE))
charArray = iconToCharArray(icon)
generateCU8IntArray(charArray)
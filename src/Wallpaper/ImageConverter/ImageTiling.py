import matplotlib.pyplot as plt
import cv2

def LoadImage(imageDir):
    # Load Image
    #img = cv2.cvtColor(cv2.imread(imageDir), cv2.COLOR_BGR2RGB)
    img = cv2.imread(imageDir)

    # Debug Show
    #plt.imshow(img)
    #plt.show()

    return img

def SplitImageIntoTiles(img):
    tiles = []

    M = 480 // 20
    N = 800 // 20

    for y in range(0, 480, M):
        for x in range(0, 800, N):
            imageSlice = img[y:y + M, x:x + N]
            imageName = "Tiles/{:d}x{:d}y.jpg".format(x, y)
            tiles.append((x, y))
            cv2.imwrite(imageName, imageSlice)

    return tiles
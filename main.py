from array import *
import cv2
import pandas as pd
import numpy as np
import pyautogui
import random


# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:13:40 2020

@author: Manish Singh
"""

img = cv2.imread("colorpic.jpg") # get image from user input
imgWidth = img.shape[1] - 40

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv("colors.csv", header=None, names=index)

r = g = b = xpos = ypos = 0


def getRGBvalue(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    xpos = x
    ypos = y
    b, g, r = img[y, x]
    b = int(b)
    g = int(g)
    r = int(r)


def colorname(B, G, R):
    minimum = 10000
    for i in range(len(df)):
        d = abs(B - int(df.loc[i, "B"])) + abs(G - int(df.loc[i, "G"])) + abs(R - int(df.loc[i, "R"]))
        if (d <= minimum):
            minimum = d
            cname = df.loc[i, "color_name"] + "Hex" + df.loc[i, "hex"]
    return cname


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", getRGBvalue)

colorsInImg = []

# add five random colors to the array of colors for the clothing item
for i in 4:
    object_x = random.random() * 10
    object_y = random.random() * 10
    mouse_x, mouse_y = pyautogui.position()
    pyautogui.moveTo(mouse_x + object_x, mouse_y + object_y, 0.25)
    cv2.imshow("Image", img)
    cv2.rectangle(img, (20, 20), (imgWidth, 60), (b, g, r), -1)
    text = colorname(b, g, r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    colorsInImg.append(text)

while True:
    cv2.imshow("Image", img)
    cv2.rectangle(img, (20, 20), (imgWidth, 60), (b, g, r), -1)
    text = colorname(b, g, r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    if (r + g + b >= 600):
        cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()


class Tops:
    # 0 row is short sleeves
    # 1 row in long sleeves
    # 2 row is jackets
    def __init__(self):
        self.tops = [[]]
    def __add__(self, type, name):
        if (type == "Short Sleeves"):
            self.tops[0].append(name)
        if (type == "Long Sleeves"):
            self.tops[1].append(name)
        if (type == "Jackets"):
            self.tops[2].append(name)

    def getSubCategory(self, type):
        if (type == "Short Sleeves"):
            return self.tops[0]
        if (type == "Long Sleeves"):
            return self.tops[1]
        if (type == "Jackets"):
            return self.tops[2]

class Dresses:
    # 0 row is dresses
    def __init__(self):
        self.dresses = [[]]

    def __add__(self, name):
        self.dresses.append[0](name)

    def getSubCategory(self, type):
        if (type == "Dresses"):
            return self.dresses[0]

class Bottoms:
    # 0 row is shorts
    # 1 row is pants
    def __init__(self):
        self.bottoms = [[]]

    def __add__(self, type, name):
        if (type == "Short"):
            self.bottoms[0].append(name)
        if (type == "Pants"):
            self.bottoms[1].append(name)

    def getSubCategory(self, type):
        if (type == "Shorts"):
            return self.bottoms[0]
        if (type == "Pants"):
            return self.bottoms[1]

class Shoes:
    # 0 row is open toe
    # 1 row is closed toe
    def __init__(self):
        self.shoes = [[]]

    def __add__(self, type, name):
        if (type == "Open Toe"):
            self.shoes[0].append(name)
        if (type == "Closed Toe"):
            self.shoes[1].append(name)

    def getSubCategory(self, type):
        if (type == "Open Toe"):
            return self.shoes[0]
        if (type == "Closed Toe"):
            return self.shoes[1]



def main():
    temperature = 0  # get from weather API
    topClothes = []
    bottomClothes = []
    dresses = []
    shoes = []
    if (temperature >= 65):
        topClothes.append(Tops.getSubCategory("Short Sleeves"))
    if (temperature < 65):
        topClothes.append(Tops.getSubCategory("Long Sleeves"))
    if (temperature < 40):
        topClothes.append(Tops.getSubCategory("Jackets"))

    if (temperature >= 60):
        bottomClothes.append(Bottoms.getSubCategory("Shorts"))
    else:
        bottomClothes.append(Bottoms.getSubCategory("Pants"))

    if (temperature >= 70):
        dresses.append(Dresses.getSubCategory("Dresses"))
        shoes.append(Shoes.getSubCategory("Open Toe"))
    else:
        shoes.append(Shoes.getSubCategory("Closed Toe"))

    index = random.random() * len(bottomClothes)
    bottomClothingItem = bottomClothes[0][index]

    tempTops = topClothes[0]
    topClothingItem = ""
    while (len(tempTops) > 0):
        index = random.random()  * len(tempTops)
        topClothingItem = tempTops[index]
        for x in bottomClothingItem.colorsInImg:
            for y in topClothingItem.colorsInImg:
                if (x > y - 40 & x < y + 40):
                    bottomClothingItem = x
                    topClothingItem = y
                    break
                if (x < 865 / 2):
                    x = x + 432
                    if (x > y - 40 & x < y + 40):
                        bottomClothingItem = x
                        topClothingItem = y
                        break
                else:
                    x = x - 432
                    if (x > y - 40 & x < y + 40):
                        bottomClothingItem = x
                        topClothingItem = y
                        break

    return topClothingItem & bottomClothingItem


if __name__ == "__main__":
    main()
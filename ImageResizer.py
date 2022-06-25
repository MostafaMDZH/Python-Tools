# mostafa.mdzh@gmail.com | @MostafaMDZH
# Usage: create a folder named "gallery" and put all your images(including subfolders) into it and run the main file with python 3 while passing the intended size(default is 1080 px):
# python3 ImageResizer.py 720 // resizes all the image's smaller sides (depending on image orientation) to 720 pixels, and resizes the image's bigger side dependent on the original ratio.

import sys
import os
from PIL import Image, ImageFont

def resize(imagePath, newMinSize):

    # open the image:
    image = Image.open(imagePath)
    width, height = image.size
    if width <= newMinSize or height <= newMinSize:
        return

    # calculate the new size:
    imageRatio = width/height
    isLandscape = imageRatio > 1
    if isLandscape:
        newHeight = newMinSize
        newWidth = int(newMinSize*imageRatio)
    else:
        newWidth = newMinSize
        newHeight = int(newMinSize/imageRatio)

    # resize and save:
    resizedImage = image.resize((newWidth,newHeight))
    resizedImage.save(imagePath)

# get the new min size:
if len(sys.argv) >= 2:
    newMinSize = int(sys.argv[1])
else:
    newMinSize = 1080

# loop through files and folders:
rootDir = os.path.dirname(os.path.realpath(__file__)) + '/gallery'
totalFiles = sum([len(files) for r, d, files in os.walk(rootDir)])
progressIndex = 0
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        progress = format(int(progressIndex*100/totalFiles))
        print('...resizing[' + progress + '%]', end="\r")
        resize(os.path.join(subdir, file), newMinSize)
        progressIndex = progressIndex + 1

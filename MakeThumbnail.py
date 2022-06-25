# mostafa.mdzh@gmail.com | @MostafaMDZH
# Usage: create a folder named "gallery" and put all your images (including subfolders) into it and 

import sys
import os
from PIL import Image, ImageDraw, ImageFont

def resize(imagePath, newMinSize):
    
    # open the image:
    image = Image.open(imagePath)
    width, height = image.size
    
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
    resizedImagePath = lastReplace(imagePath, '.', '.min.', 1)
    resizedImage.save(resizedImagePath)

def lastReplace(text, old, new, occurrence):
    list = text.rsplit(old, occurrence)
    return new.join(list)

# get the thumbnail size:
if len(sys.argv) >= 2:
    newMinSize = int(sys.argv[1])
else:
    newMinSize = 300

# loop through files and folders:
rootDir = os.path.dirname(os.path.realpath(__file__)) + '/gallery'
totalFiles = sum([len(files) for r, d, files in os.walk(rootDir)])
progressIndex = 0
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        progress = format(int(progressIndex*100/totalFiles))
        print('...making thumbnails[' + progress + '%]', end="\r")
        resize(os.path.join(subdir, file), newMinSize)
        progressIndex = progressIndex + 1
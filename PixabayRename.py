# mostafa.MDZH@gmail.com | @MostafaMDZH

from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont

def rename(imagePath):

    # splitting directory, name, and format:
    imagePath_Split = imagePath.rsplit("/", 1)
    imageDir = imagePath_Split[0]
    imageNameFormat = imagePath_Split[1]
    imageNameFormat_Split = imageNameFormat.rsplit(".", 1)
    imageName = imageNameFormat_Split[0]
    imageFormat = imageNameFormat_Split[1]

    # replace the underline and space with dash:
    newName = imageName.replace("_", "-")
    newName = newName.replace(" ", "-")

    # split to an array:
    newName = newName.rsplit("-", -1)

    # removing the numbers and capitalizing first letter:
    for i, word in enumerate(newName):
        if word.isnumeric():
            newName[i] = ""
        else:
            newName[i] = newName[i].capitalize()
    
    # filtering empty parts of the array:
    newName = filter(None, newName)

    # rejoining with space:
    space = " "
    newName = space.join(newName)

    # rejoining the format:
    newName = newName + "." + imageFormat

    # join the directory:
    newName = imageDir + "/" + newName

    # check file exists:
    finalName = newName
    myFile = Path(finalName)
    index = 2
    while myFile.is_file():
        finalName = lastReplace(newName, ".", "." + str(index) + ".", 1)
        myFile = Path(finalName)
        index = index + 1
    
    # save:
    os.rename(imagePath, finalName)

def lastReplace(text, old, new, occurrence):
    list = text.rsplit(old, occurrence)
    return new.join(list)

# loop through files and folders:
rootDir = os.path.dirname(os.path.realpath(__file__)) + '/Gallery'
totalFiles = sum([len(files) for r, d, files in os.walk(rootDir)])
progressIndex = 0
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        progress = format(int(progressIndex*100/totalFiles))
        print('...renaming[' + progress + '%]', end="\r")
        rename(os.path.join(subdir, file))
        progressIndex = progressIndex + 1
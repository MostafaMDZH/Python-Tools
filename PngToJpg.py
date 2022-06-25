# mostafa.mdzh@gmail.com | @MostafaMDZH
# Usage: create a folder named "gallery" and put all your images(including subfolders) into it and run the main file with python 3.

import os
from PIL import Image

def convert(imagePath):

    if '.png' in imagePath:
        try:
            image = Image.open(imagePath)
            canvas = Image.new("RGB", image.size, (255,255,255))
            canvas.paste(image, image)
            newPath = imagePath.replace(".png", ".jpg")
            canvas.save(newPath)
            os.remove(imagePath)
        except ValueError:
            print('Cannot Convert: ' + imagePath)

# loop through files and folders:
rootDir = os.path.dirname(os.path.realpath(__file__)) + '/gallery'
totalFiles = sum([len(files) for r, d, files in os.walk(rootDir)])
progressIndex = 0
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        progress = format(int(progressIndex*100/totalFiles))
        print('...renaming[' + progress + '%]', end="\r")
        convert(os.path.join(subdir, file))
        progressIndex = progressIndex + 1

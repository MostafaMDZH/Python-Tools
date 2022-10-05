# mostafa.mdzh@gmail.com | @MostafaMDZH
# Usage: create a folder named "gallery" and put all your images(including subdirectories) into it and 

import sys
import os
from PIL import Image, ImageDraw, ImageFont

def watermark(sourcePath, text):

    # if it is a thumbnail, skip
    if '.min.' in sourcePath:
        return

    # open the source image:
    sourceImage = Image.open(sourcePath)
    width, height = sourceImage.size

    # create a canvas:
    canvas = Image.new("RGBA", sourceImage.size)
    canvasObj = ImageDraw.ImageDraw(canvas, "RGBA")

    # font and size:
    font = ImageFont.truetype('ubuntu_bold.ttf', 50)
    textWidth, textHeight = canvasObj.textsize(text, font)

    # calculate the text placement:
    x = (width/2) - (textWidth/2)
    y = ((height*4)/5) - (textHeight/2)

    # add the text:
    canvasObj.text((x, y), text, (255,255,255), font=font)
    alphaMask = canvas.convert("L").point(lambda x: min(x, 60))
    canvas.putalpha(alphaMask)

    # save
    sourceImage.paste(canvas, None, canvas)
    sourceImage.save(sourcePath)

# get the text:
if len(sys.argv) >= 2:
    text = sys.argv[1]
else:
    print('error: please pass the text you want to watermark')
    quit()

# loop through files and folders:
rootDir = os.path.dirname(os.path.realpath(__file__)) + '/gallery'
totalFiles = sum([len(files) for r, d, files in os.walk(rootDir)])
progressIndex = 0
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        progress = format(int(progressIndex*100/totalFiles))
        print('...watermarking[' + progress + '%]', end="\r")
        watermark(os.path.join(subdir, file), text)
        progressIndex = progressIndex + 1

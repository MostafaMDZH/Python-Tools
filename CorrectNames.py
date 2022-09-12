# mostafa.mdzh@gmail.com | @MostafaMDZH

import json
from pathlib import Path
import os

# open the list:
listFile = open('list.json')
list = json.load(listFile)
num = 1

for i in list['list']:
    
    # name & dir:
    oldName = i["oldName"]
    dir     = i["path"   ]
    newName = i["newName"]
    
    # path
    oldPath = Path("gallery" + dir + "/" + oldName)
    newPath = Path("gallery" + dir + "/" + newName)
    
    # loop to files:
    for j in range(1, 100):
        
        # main file:
        oldFullName = str(oldPath) + "." + str(j) + ".jpg"
        file = Path(oldFullName)
        if file.is_file():
            newFullName = str(newPath) + "." + str(j) + ".jpg"
            os.rename(oldFullName, newFullName)
            print('renamed[' + str(num) + ']: ' + oldFullName + '     to: ' + newFullName)
        
        # .min file
        oldFullName = str(oldPath) + "." + str(j) + ".min.jpg"
        file = Path(oldFullName)
        if file.is_file():
            newFullName = str(newPath) + "." + str(j) + ".min.jpg"
            os.rename(oldFullName, newFullName)
            print('renamed[' + str(num) + ']: ' + oldFullName + ' to: ' + newFullName)

        else:
            if j != 1: num += 1
            break
    
    if j == 1:
        print('not found: ' + str(oldPath))
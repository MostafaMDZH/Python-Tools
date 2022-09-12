# mostafa.mdzh@gmail.com | @MostafaMDZH
# Usage: create a folder named "files" alongside the main file and put all your files and folders into it and then run the main file with python 3.

from pathlib import Path
import os

gt = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

# loop through files and folders:
rootDir = os.path.dirname(os.path.realpath(__file__)) + '/gallery'
totalFiles = sum([len(files) for r, d, files in os.walk(rootDir)])
progressIndex = 0
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        firstLetter = file[0]
        firstLetter = firstLetter.lower()
        gt = gt + 1 
        if firstLetter == 'a':
            a = a + 1
        elif firstLetter == 'b':
            b = b + 1
        elif firstLetter == 'c':
            c = c + 1
        elif firstLetter == 'd':
            d = d + 1
        elif firstLetter == 'e':
            e = e + 1
        elif firstLetter == 'f':
            f = f + 1
        elif firstLetter == 'g':
            g = g + 1
        elif firstLetter == 'h':
            h = h + 1
        elif firstLetter == 'i':
            i = i + 1
        elif firstLetter == 'j':
            j = j + 1
        elif firstLetter == 'k':
            k = k + 1
        elif firstLetter == 'l':
            l = l + 1
        elif firstLetter == 'm':
            m = m + 1
        elif firstLetter == 'n':
            n = n + 1
        elif firstLetter == 'o':
            o = o + 1
        elif firstLetter == 'p':
            p = p + 1
        elif firstLetter == 'q':
            q = q + 1
        elif firstLetter == 'r':
            r = r + 1
        elif firstLetter == 's':
            s = s + 1
        elif firstLetter == 't':
            t = t + 1
        elif firstLetter == 'u':
            u = u + 1
        elif firstLetter == 'v':
            v = v + 1
        elif firstLetter == 'w':
            w = w + 1
        elif firstLetter == 'x':
            x = x + 1
        elif firstLetter == 'y':
            y = y + 1
        elif firstLetter == 'z':
            z = z + 1
        else:
            print('file doesn\'t start with letter: ' + file)

# print the result:
print('A: ' + str(a))
print('B: ' + str(b))
print('C: ' + str(c))
print('D: ' + str(d))
print('E: ' + str(e))
print('F: ' + str(f))
print('G: ' + str(g))
print('H: ' + str(h))
print('I: ' + str(i))
print('J: ' + str(j))
print('K: ' + str(k))
print('L: ' + str(l))
print('M: ' + str(m))
print('N: ' + str(n))
print('O: ' + str(o))
print('P: ' + str(p))
print('Q: ' + str(q))
print('R: ' + str(r))
print('S: ' + str(s))
print('T: ' + str(t))
print('U: ' + str(u))
print('V: ' + str(v))
print('W: ' + str(w))
print('X: ' + str(x))
print('Y: ' + str(y))
print('Z: ' + str(z))
print('Total: ' + str(gt))

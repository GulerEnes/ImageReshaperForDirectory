from os.path import splitext
from os import walk
import easygui as eg
import cv2 as cv

path = eg.diropenbox()
fileExt = list(input("File extentions (write comma seperated): ").split(","))
new_shape = (int(input("width: ")), int(input("height: ")))

try:
    _, _, filenames = next(walk(path))
    # print(filenames)
    for f in filenames:
        oldName, ext = splitext(f)
        if ext[1:] in fileExt:
            filepath = path + '/' + f
            img = cv.imread(filepath)
            img = cv.resize(img, new_shape)
            cv.imwrite(filepath, img)
            print("Saved:", filepath)


except Exception as e:
    print("Error:", e)

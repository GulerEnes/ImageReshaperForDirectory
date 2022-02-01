from os.path import splitext
from os import walk
import easygui as eg
from cv2 import imread, imwrite, resize

path = eg.diropenbox()
fileExt = list(input("File extentions (write comma seperated): ").split(","))
new_shape = (int(input("width: ")), int(input("height: ")))

try:
    _, _, filenames = next(walk(path))

    for f in filenames:
        _, ext = splitext(f)
        if ext[1:] in fileExt:
            filepath = path + '/' + f
            img = imread(filepath)
            img = resize(img, new_shape)
            imwrite(filepath, img)
            print("Saved:", filepath)


except Exception as e:
    print("Error:", e)

import cv2 as cv
import numpy as np
import os
import sys
import shutil
from datetime import datetime


def croper(image, resize):
    img = cv.imread(image)
    img = cv.resize(img, resize)
    return img

def fileExist():    
    BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
    new_dir = os.path.join(BASE_DIR, "x")

    cwd = os.getcwd()
    items = os.listdir(cwd)
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    timestamp = timestamp.replace(":", ".")


    if 'Cropped' in items:
        cropPath = os.path.join(cwd, "Cropped")
        newName = os.path.join(cwd, f"Cropped_{timestamp}")
        os.rename(cropPath, newName)
        try: 
            os.mkdir(cwd + "/backup/")
        except:
            print("Dir exists")

        newDir = os.path.join(cwd, "backup")
        shutil.move(newName, newDir) 
        print("Moved to backup")
        # print(cropPath, newDir, newName, sep="\n")

    else:
        print("Creating a dir")


def main():
    cropped = 0
    NotCropped = 0
    BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
    fileExist()
    new_dir = os.path.join(BASE_DIR, "Cropped")
    try:
        image_dir = os.path.join(BASE_DIR, sys.argv[1])
        os.mkdir(new_dir)


    except OSError as error: 
        print(error)

    except IndexError:
        print("PLease add the directory name to the arguments")
        sys.exit(1)

    x, y = int(sys.argv[2]), int(sys.argv[3])

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('png') or file.endswith('jpg'):
                path = os.path.join(root, file)
                new_path = os.path.join(new_dir, file)
                # print(path)
                try:
                    img = croper(path, (x, y))
                    cv.imwrite(new_path, img)
                    print(f"{file} Cropped")
                    cropped += 1
                    # print("".join((file)))
                except:
                    print(f"{file} NOT CROPPED")
                    NotCropped += 1
    total = cropped + NotCropped

    print("CROPPING COMPLETE")
    print(f"Cropped {cropped} out of {total} images")
    print(f"Unable to crop {NotCropped} images")
    print(f"Try renaming the {NotCropped} images")


if __name__ == '__main__':
    main()
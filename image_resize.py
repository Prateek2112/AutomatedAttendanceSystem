import os
import cv2

# path containing the required folders of images
path = 'Validation/'

# New path where resized images need to be saved
new = 'resizedval/'
sortedFaces = sorted(os.listdir(path))
for i in sortedFaces:
    if not os.path.exists(new + i):
        print("New directory created")
        os.makedirs(new + i)

d = 0
for i in sortedFaces:
    for j in os.listdir(path + i + '/'):
        img = cv2.resize(cv2.imread(path + i + '/' + j), (32, 32), cv2.INTER_CUBIC)
        cv2.imwrite(new + i + '/' + str(d) + '.jpg', img)
        d += 1

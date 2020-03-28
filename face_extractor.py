pip install mxnet

# coding: utf-8
import mxnet as mx
from mtcnn_detector import MtcnnDetector
import cv2
import os
import glob
import time

detector = MtcnnDetector(model_folder='model', ctx=mx.cpu(0), num_worker = 4 , accurate_landmark = False)

iter = 0

#Creating an array of images in a folder named 'trial1'
images = [cv2.imread(file) for file in glob.glob("trial1/*.jpg")]

for img in images:

  results = detector.detect_face(img)

  if results is not None:

    total_boxes = results[0]
    points = results[1]

    draw = img.copy()
    #Drawing boxes around faces
    for b in total_boxes:
        cv2.rectangle(draw, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (255, 255, 255))

    #Detecting features of face (eyes, mouth, nose)    
    for p in points:
        for i in range(5):
            cv2.circle(draw, (p[i], p[i + 5]), 1, (0, 0, 255), 2)

    cv2_imshow(draw)
    cv2.waitKey(0)

    #Creating subpaths inside a master folder 'trial-1f'
    facepath = 'trial-1f/faces' + str(iter)
    if not os.path.exists(facepath):
      print("New directory created")
      os.makedirs(facepath)
     

    #Converting the array of images to list
    boxes = total_boxes.tolist()


    d=0
    #Iterating over all detected images and cropping out
    for box in boxes:
    # print(int(coord), end=" ", flush=True)
      crop = img[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
      cv2.imwrite(facepath + '/' + str(d) + '.jpg', crop)
      d += 1


    iter += 1


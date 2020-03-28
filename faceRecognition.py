CATEGORIES = ['Aditya', 'Akansha', 'Akashnil', 'Ameya', 'Aravind', 'Basu', 'Divyanshu', 'Ghayathri', 'Hitesh', 'Jay', 'Ganguly',
              'Manral', 'Mayank', 'Mohan', 'Moumi', 'Moumita', 'Pratik C', 'Praveen', 'Priyanka', 'Rahul', 'Satendra', 'Soorma',
              'Soumya Kartik', 'Vivek Kumar', 'Vipul', 'Vivek John']

import glob
import os

import cv2
import mxnet as mx
import numpy as np
import tensorflow as tf

from mtcnn_detector import MtcnnDetector

# Extracting images from Video
d = 0
# n is the seconds value (i.e) every 35th second of the video,a frame will be saved
n = 35
x = n * 1000

if not os.path.exists('trial1'):
    print("New directory created")
    os.makedirs('trial1')


for i in range(x, (x * 12) + 10, x):

    vidcap = cv2.VideoCapture('ch003_20200117112744t23E9.mp4')
    vidcap.set(cv2.CAP_PROP_POS_MSEC, i)
    success, image = vidcap.read()
    if success:
        cv2.imwrite("trial1" + '/' + str(d) + ".jpg", image)  # save frame as JPEG file
        # cv2.waitKey()
        d += 1

#Defining an object of the MTCNNDetector Model
detector = MtcnnDetector(model_folder='model', ctx=mx.cpu(0), num_worker=4, accurate_landmark=False)


def fetchFaces():
    iter = 0
    facelist = []
    model = tf.keras.models.load_model("face.model")
    # Creating an array of images in a folder named 'trial1'
    images = [cv2.imread(file) for file in glob.glob("trial1/*.jpg")]
    for img in images:
        results = detector.detect_face(img)

        if results is not None:
            total_boxes = results[0]
            points = results[1]
            draw = img.copy()
            # Drawing boxes around faces
            for b in total_boxes:
                cv2.rectangle(draw, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (255, 255, 255))
                # Detecting features of face (eyes, mouth, nose)
            for p in points:
                for i in range(5):
                    cv2.circle(draw, (p[i], p[i + 5]), 1, (0, 0, 255), 2)
            cv2.imshow("draw", draw)
            # cv2.waitKey()
            # Creating subpaths inside a master folder 'trial-1f'
            facepath = 'trial-1f'
            if not os.path.exists(facepath):
                print("New directory created")
                os.makedirs(facepath)
            # Converting the array of images to list
            boxes = total_boxes.tolist()
            d = 0
            # Iterating over all detected images and cropping out
            for box in boxes:
                # print(int(coord), end=" ", flush=True)
                crop = img[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                cv2.imwrite(facepath + '/' + str(d) + '.jpg', crop)
                d += 1
            det = 'trial-1f'
            for im in os.listdir(det):
                pic = cv2.resize(cv2.imread(det + '/' + im), (32, 32), cv2.INTER_CUBIC)
                img1 = pic / 255.

                pred = model.predict(img1.reshape(-1, 32, 32, 3))

                # print(max(pred))
                facelist.append(CATEGORIES[np.argmax(pred)])
            iter += 1
    #os.remove('trial-1f')
    return (facelist)

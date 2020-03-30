# Automated-Attendance-System

The objective of this project is to process live video-stream of students in a classroom and update the attendance of the students in a Google Sheet.
The project was coded in Python 3.7 using OpenCv 4.2.0, mxnet, TensorFlow, Numpy and Tkinter libraries.
The file in the directory are:
* **python.py** : This is the main code that integrates the all python codes with Google Sheets by calling the other function modules developed.
* **connection.py** : This file authorizes the link between Python - Google Sheets using a .json file.
* **initialStudentRecord.py** : This file initializes the record containing the names of all the students enrolled in that particular class.
* **faceRecognition.py** : This is the main code that does the following using fetchFaces() function:
    * Detects and fetches face images from a 'Local Video File' or a 'Live Video Stream' using MTCNN Detector.
    * Passes these faces through a trained model for prediction.
    * Creates a list of all students detected and recognized from the video feed.
* **Face_Extractor.ipynb** : This notebook file (Google Colab) was used to extract multiple faces of each person that would later be used for training. ***face_extractor.py*** is just the python version of this notebook.
* **helper.py & mtcnn_detector.py** : These files were taken from a GitHub repository(reference links below). These python files are a part of the face detection algorithm, that draw bounding boxes and crop out the faces.
* **training.ipynb** : This notebook file (Google Colab) was used to train the faces of all students of the class by using customized VGG19 model. ***training.py*** is just the python version of this notebook.
* The **model** folder contains all the dependancies (params, json, caffemodel and prototxt) that are used my MTCNN detector.

## Getting Started
### Prerequisites

The local machine needs to be installed with Python 3.7 with all OpenCv, Tensorflow and Numpy Libraries.
Training the images requires a lot of memory and GPU, which is easily available with Google Collaboratory (Linux Based).
The MTCNN module implements bounding boxes and helps in extracting information of all the faces detected in an image.

## Built With
* [OpenCV](http://docs.opencv.org/4.2.0/) - Implementation of Algorithms
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - GUI Implementation
* [Numpy](http://www.numpy.org/) - Used to manage computations.
* [Tensorflow](https://www.tensorflow.org/install/pip) - Used to train and build models.
* [Gspread](https://gspread.readthedocs.io/en/latest/) - Used to integrate Google Sheets with Python API.

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
* **image_resize.py** : This code uses OpenCV Bicubic Interpolation to resize different images of different pixel values to 32x32. This is done to make the images more clear and easy to train.
* **helper.py & mtcnn_detector.py** : These files were taken from a GitHub repository(reference links below). These python files are a part of the face detection algorithm, that draw bounding boxes and crop out the faces.
* **training.ipynb** : This notebook file (Google Colab) was used to train the faces of all students of the class by using customized VGG19 model. ***training.py*** is just the python version of this notebook.
* **gui.py** : This python file contains the user interface code that is used to initiate the entire process.
* The **model** folder contains all the dependancies (params, json, caffemodel and prototxt) that are used my MTCNN detector.
* [Input Video and Trained Model](https://drive.google.com/open?id=1seX9yM4ehsVJFg7SmX3AAnxdPXeFoeVs)
* [Face Detection.json](https://drive.google.com/open?id=1Er_CyWJGUkql3tnN3yLguaH8nKoqv_KW)
* **Face Detection.json** : This is an important .json file to authorise and intiate a link between Python and a specific Google Sheet. A YouTube link can be found in the acknowledgements that can guide you in generating your own .json file.

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

## WorkFlow of the Program
The whole prototype is made up of several codes which are interlinked to each other in a sequential way. 
* Triggering the GUI first launches the code which establishes connection with Google Sheets through GSpread library of Google. 
* The Google Spreadsheet gets populated with a list of all students enrolled in the class and their attendance gets marked as 0 initially.
* Now the video stream passes through the program that uses OpenCV to extract few frames from the video. 
* These images flow through the MTCNN model, that extracts faces and puts them into a folder. 
* This folder is read by the pre-trained VGG19 model and predictions are done. 
* A list gets created containing predictions from all the frames. 
* This list passes through the Python - Gspread connection and attendance of the detected faces are updated to 1.

## Acknowledgements
The following blogs were helpful for this project:
* [Face Detection](https://github.com/YYuanAnyVision/mxnet_mtcnn_face_detection)
* [Python-Google Sheets Integration](https://www.youtube.com/watch?v=cnPlKLEGR7E&t=524s)
* [Understanding CNN Architecture](https://www.kaggle.com/uysimty/keras-cnn-dog-or-cat-classification)

Refer to the following papers for deeper understanding:
* Mostafa Mehdipour Ghazi and Hazim Kemal Ekenel, "A Comprehensive Analysis of Deep Learning Based Representation for Face Recognition", The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, IEEE, 2016.
* Shubhobrata Bhattacharya, Gowtham Sandeep Nainala, Prosenjit Das and Aurobinda Routray, "Smart Attendance Monitoring System (SAMS): A Face Recognition Based Attendance System for Classroom Environment",
2018 IEEE 18th International Conference on Advanced Learning Technolo- gies (ICALT), IEEE, July 2018.

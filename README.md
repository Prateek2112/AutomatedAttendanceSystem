# Automated-Attendance-System

The objective of this project is to process live video-stream of students in a classroom and update the attendance of the students in a Google Sheet.
The project was coded in Python 3.7 using OpenCv 4.2.0, mxnet, TensorFlow and Numpy libraries.
The file in the directory are:
* python.py : This is the main code that integrates the all python codes with Google Sheets by calling the other function modules developed.
* connection.py : This file authorizes the link between Python - Google Sheets using a .json file.
* initialStudentRecord.py : This file initializes the record containing the names of all the students enrolled in that particular class.

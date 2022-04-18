# OpenCV_materials

## 1. Installation

* (a) Make a virtual environment in python, the name of my virtual environment is 'cv'
py -m pip install --user virtualenv
C:\venvs>py -m venv cv

* (b) Activate the virtual environment you made in the previous step
C:\venvs>.\cv\Scripts\activate

* (c) Install the following packages:
(cv) C:\venvs>py -m pip install opencv-python
(cv) C:\venvs>py -m pip install opencv-contrib-python


* (d) Besides installing OpenCV, we cover the installation of the following package:

(cv) C:\venvs>pip freeze
caer==2.0.8
cycler==0.11.0
fonttools==4.32.0
kiwisolver==1.4.2
matplotlib==3.5.1
numpy==1.22.3
opencv-contrib-python==4.5.5.64
opencv-python==4.5.5.64
packaging==21.3
Pillow==9.1.0
pyparsing==3.0.8
python-dateutil==2.8.2
six==1.16.0

##Caer is a lightweight, high-performance Vision library for high-performance AI research. It simplifies your approach towards Computer Vision by abstracting away unnecessary boilerplate code giving you the flexibility to quickly prototype deep learning models and research ideas.

$ pip install caer



## 2. Basic Concepts:
* Reading Images and Video (read.py)
* Resizing and Rescaling Images and Video Frames (rescale.py)
* Drawing Shapes and Placing text on images (draw.py)
* 5 Essential Methods in OpenCV (basic.py)
* Image Transformations (transformation.py)
* Contour Detection (contours.py)
## 3. Advanced Concepts:
* Switching between Colour Spaces (RGB, BGR, Grayscale, HSV and Lab) (spaces.py)
* Splitting and Merging Colour Channels (split.merge)
* Blurring (smoothing.py)
* BITWISE operations (bitwise.py)
* Masking (masking.py)
* Histogram Computation (histogram.py)
* Thresholding/Binarizing Images (threshold.py)
* Advanced Edge Detection (gradient.py)
## 4. Face Detection and Recognition
* Face Detection using Haar Cascades (face_detect.py)
* Face Detection using webcam (face_detect_webcam.py)
* Face Recognition using OpenCV's LBPHFaceRecognizer algorithm (face_recognition.py)



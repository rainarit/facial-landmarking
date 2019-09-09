# Facial Landmarking
#### [facial_landmarking.py](https://github.com/rainarit/FacialLandmarking/blob/master/facial_landmarking.py) #### 
__Completed :white_check_mark:__

This is a Python script which utilizes the **[shape_predictor_81_face_landmarks.dat](https://github.com/rainarit/FacialLandmarking/blob/master/shape_predictor_81_face_landmarks.dat)** file to  facially landmark 81 locations of our face. The dlib library is used to first detect the faces and the dat file is used for the landmarks. 

An extra touch to the script was the use of counting how many blinks were made. This was done via the Ear-Aspect-Ratio(EAR) which makes use of the 6 coordinates surrounding the eyes. The following GIF gives a representation of the project.

<img src='http://g.recordit.co/fTUgWGwohA.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

# Installation ##
### Requirements ###
The following software libraries/frameworks should be installed:
* [Python](https://www.python.org/downloads/) 3.3+ or Python 2
* [imutils](https://pypi.org/project/imutils/) library
* [datetime](https://docs.python.org/3/library/datetime.html) library
* [time](https://docs.python.org/2/library/time.html) library
* [dlib](https://pypi.org/project/dlib/) package
* [cv2](https://pypi.org/project/opencv-python/) package
### Installation Options ###
The libraries and frameworks displayed above could be installed in the following direction:

`pip3 install 'framework/library'`
## Usage ##
1. Download [facial_landmarking.py](https://github.com/rainarit/FacialLandmarking/blob/master/facial_landmarking.py). 
2. Download [shape_predictor_81_face_landmarks.dat](https://github.com/rainarit/FacialLandmarking/blob/master/shape_predictor_81_face_landmarks.dat)
3. Go to your Python IDLE and insert: 
`python3 facial_landmarking.py`

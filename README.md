# FacialLandmarking
#### [facial_landmarking.py](https://github.com/rainarit/FacialLandmarking/blob/master/facial_landmarking.py) #### 
__Completed :white_check_mark:__

This is a Python script which utilizes the **[shape_predictor_81_face_landmarks.dat](https://github.com/rainarit/FacialLandmarking/blob/master/shape_predictor_81_face_landmarks.dat)** file to  facially landmark 81 locations of our face. The dlib library is used to first detect the faces and the dat file is used for the landmarks. 

An extra touch to the script was the use of counting how many blinks were made. This was done via the Ear-Aspect-Ratio(EAR) which makes use of the 6 coordinates surrounding the eyes. The following GIF gives a representation of the project.

<img src='http://g.recordit.co/fTUgWGwohA.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

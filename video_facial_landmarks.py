# Imports
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
 
# Initializing dlib's face detector (HOG-based)
# Creating the facial shape predictor using the 'shape_predictor_81_face_landmarks.dat' file
print("Initializing Facial Landmarking Predictor ->")
#Detecting the frontal faces
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_81_face_landmarks.dat')

# Initializing the camera sensor to warm up
print("Camera Sensor Warming Up ->")
vs = VideoStream(0).start()
time.sleep(2.0)

# Looping over all the frames from the webcam stream
while True:
    # Grabbing the frames
	frame = vs.read()
    # Setting the frame size to 500
	frame = imutils.resize(frame, width=500)

	# Detecting the faces from the frame
	rects = detector(frame, 0)

	# Looping throughe each face detection
	for rect in rects:
		shape = predictor(frame, rect)
		shape = face_utils.shape_to_np(shape)

		# Looping over the facial lanmarks based on their (x,y) coordinates
        # Drawing a red circle over those landmarks
		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
	  
	# Showing the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# Break from loop/end when the 'q' is pressed
	if key == ord("q"):
		break
        
# Destroying the windows once the frame display is over
cv2.destroyAllWindows()
vs.stop()

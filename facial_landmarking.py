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
# Creating the facial shape predictor using the 'shape_predictor_68_face_landmarks.dat' file
print("Initializing Facial Landmarking Predictor ->")
#Detecting the frontal faces
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('/Users/rraina/Desktop/real-time-facial-landmarks/shape_predictor_68_face_landmarks.dat')

# Initializing the camera sensor to warm up
print("Camera Sensor Warming Up ->")
vs = VideoStream(0).start()
time.sleep(2.0)

blink_count = 0

# Looping over all the frames from the webcam stream
while True:
    # Grabbing the frames
	frame = vs.read()
    # Setting the frame size to 500
	frame = imutils.resize(frame, width=500)
	cv2.putText(frame, "Blink Count = " + str(blink_count), (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

	# Detecting the faces from the frame
	rects = detector(frame, 0)

	# Looping through each face detection
	for rect in rects:
		shape = predictor(frame, rect)
		shape = face_utils.shape_to_np(shape)

		# Looping over the facial landmarks based on their (x,y) coordinates
        # Drawing a red circle over those landmarks
		count = 0
		top_right_1 = 0
		bottom_right_1 = 0
		top_right_2 = 0
		bottom_right_2 = 0
		for (x, y) in shape:
			print(float(x))           
			count = count + 1
			cv2.circle(frame, (x, y), 0, (0, 0, 255), -1)
			if (count == 38):
				top_right_1 = y
			if (count == 42):
				bottom_right_1 = y
			if (count == 39):
				top_right_2 = y
			if (count == 41):
				bottom_right_2 = y
		if (bottom_right_1 - top_right_1 < 3 and bottom_right_2 - top_right_2 < 3):
			blink_count = blink_count + 1
	  
	# Showing the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# Break from loop/end when the 'q' is pressed
	if key == ord("q"):
		break
        
# Destroying the windows once the frame display is over
cv2.destroyAllWindows()
vs.stop()

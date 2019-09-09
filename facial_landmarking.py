# Imports
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import imutils
import time
import dlib
import cv2

# import the necessary packages
from scipy.spatial import distance as dist

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear
 
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
total = 0

# Looping over all the frames from the webcam stream
while True:
    # Grabbing the frames
	frame = vs.read()
    # Setting the frame size to 500
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.putText(frame, "Blink Count = " + str(total), (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

	# Detecting the faces from the frame
	rects = detector(frame, 0)
    

	# Looping through each face detection
	for rect in rects:
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
        
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
 
		# average the eye aspect ratio together for both eyes
		ear = (leftEAR + rightEAR) / 2.0
        
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
		if ear < 0.25:
			blink_count += 1
 
		# otherwise, the eye aspect ratio is not below the blink
		# threshold
		else:
			# if the eyes were closed for a sufficient number of
			# then increment the total number of blinks
			if blink_count >= 3:
				total += 1
 
			# reset the eye frame counter
			blink_count = 0
            
		# Looping over the facial landmarks based on their (x,y) coordinates
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

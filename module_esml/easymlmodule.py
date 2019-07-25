#coded by Sahil Panindre
def esml(String_data):
	import cv2
	import numpy as np
	from win32com.client import Dispatch

	def still_cam_intruder_security():
		# Video Capture 
		capture = cv2.VideoCapture(0)
		#capture = cv2.VideoCapture("demo.mov")

		# History, Threshold, DetectShadows 
		# fgbg = cv2.createBackgroundSubtractorMOG2(50, 200, True)
		fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)

		# Keeps track of what frame we're on
		frameCount = 0

		while(1):
			# Return Value and the current frame
			ret, frame = capture.read()

			#  Check if a current frame actually exist
			if not ret:
				break

			frameCount += 1
			# Resize the frame
			resizedFrame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

			# Get the foreground mask
			fgmask = fgbg.apply(resizedFrame)

			# Count all the non zero pixels within the mask
			count = np.count_nonzero(fgmask)

			print('Frame: %d, Pixel Count: %d' % (frameCount, count))

			# Determine how many pixels do you want to detect to be considered "movement"
			# if (frameCount > 1 and cou`nt > 5000):
			if (frameCount > 1 and count > 5000):
				print('Security Alert')
				cv2.putText(resizedFrame, 'Security Alert', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
				speak = Dispatch("SAPI.SpVoice")
				speak.Speak("Security Alert")

			cv2.imshow('Frame', resizedFrame)
			cv2.imshow('Mask', fgmask)


			k = cv2.waitKey(1) & 0xff
			if k == 27:
				break

		capture.release()
		cv2.destroyAllWindows()
	def face_detection_with_builtin_webcam():
		cap = cv2.VideoCapture(0)	
		# Create the haar cascade
		faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

		while(True):
			# Capture frame-by-frame
			ret, frame = cap.read()

			# Our operations on the frame come here
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			# Detect faces in the image
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30)
				#flags = cv2.CV_HAAR_SCALE_IMAGE
			)

			print("Found {0} faces!".format(len(faces)))

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


			# Display the resulting frame
			cv2.imshow('frame', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break					
		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()
	def face_detection_with_given_image():
		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

		img = cv2.imread(input("give the image name if image is in same folder or path if the image is in different folder"))
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('img',img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	data_from_user = print(String_data)
	if String_data == "still_cam_intruder_security":
		print("ok")
		still_cam_intruder_security()
	if String_data == "face_detection_with_builtin_webcam":
		face_detection_with_builtin_webcam()
	if String_data == "face_detection_with_given_image":
		face_detection_with_given_image()
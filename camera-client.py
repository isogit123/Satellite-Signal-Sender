import numpy as np
import cv2
import pytesseract
import socketio
import base64

sio = socketio.Client()

points = {'x1': 0, 'y1': 0, 'x2': 5, 'y2': 5}
#sendImage=0, no image sent
#sendImage=1, send full image
#sendImage=2, cropped image is sent
sendImage = 0
@sio.event
def connect():
    print('Socket IO client connection established')

@sio.event
def roi(data):
	global points
	global sendImage
	print('New points received: ', data)
	points = data
	sendImage = 2

@sio.event
def resetRoi(data):
	global sendImage
	print('Reset ROI request received.')
	sendImage = 1
	
    
@sio.event
def disconnect():
	print('Socket IO client disconnected from server')

def emitImage(img):
	retval, buffer = cv2.imencode('.webp', img)
	img_as_text = base64.b64encode(buffer)
	sio.emit('image', {'img': 'data:image/webp;base64,' + str(img_as_text)[2:len(img_as_text)+2]})

sio.connect('http://localhost:5022')

cap = cv2.VideoCapture(0)
config = ("-l eng --oem 1 --psm 7")

while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
	#Selects region of interest selected by receiver
	roi = frame[points['y1']:points['y2'], points['x1']:points['x2']]
    # Read text from ROI
	text = pytesseract.image_to_string(roi, config=config)
	#Send text using SocketIO
	sio.emit('receiveSignal', {'signal': text})
	#Send either full image or roi to receiver upon request, each is sent only once
	if sendImage == 1:
		emitImage(frame)
	elif sendImage == 2:
		if roi.shape[0] == abs(points['x2']-points['x1']):
			emitImage(roi)
		else:
			roi = frame[points['y1']:points['y2'], points['x1']:points['x2']]
			emitImage(roi)
	sendImage = 0
	
    # Display the resulting frame
	cv2.imshow('image',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


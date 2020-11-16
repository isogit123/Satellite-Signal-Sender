# Satellite Signal Sender
Reads the satellite signal from TV using a webcam and sends it as text to a client running an HTML page for Satellite dish positioning.
Useful when monitoring satellite signal strength when positioning a satellite dish.
Signal is captured using webcam and sent over network as text to decrease bandwidth usage.
## Implementation Details
```camera-client.py``` runs on the sender. It extracts the text using pytesseract and sends it to the receiver using SocketIO. <br />
```server.js``` contains a SocketIO NodeJS server to send the extracted text to the receiver. <br />
```receiver.html``` accessed by the receiver using any browser. It receives the text and is used to set the region in which the signal is located in the image. <br />
## Installing Dependencies
- Install Tesseract OCR by following the tutorial at https://tesseract-ocr.github.io/tessdoc/Home.html
- Install Python dependencies by running
```
python -m pip install opencv-python numpy pytesseract "python-socketio[client]"
```
- Install NodeJS from https://nodejs.org/
## Usage
- Open terminal and navigate to the project's directory.
- Run the NodeJS server by:
```
node server.js
```
- Run the Python client using:
```
python camera-client.py
```
- Open http://127.0.0.1:5022 using any browser.

## Demo
Demo video available at https://youtu.be/BZ5C8OdQoHE <br />
I recorded the signal from TV using a webcam and used it for testing.

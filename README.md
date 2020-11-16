# Satellite-Signal-Sender
Reads the satellite signal from TV using a webcam and sends it as text for Satellite dish positioning.
Useful when monitoring satellite signal strength when positioning a satellite dish.
Signal is captured using webcam and sent over network as text to decrease bandwidth usage.
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

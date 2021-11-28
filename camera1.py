# camera.py

import picamera
import StringIO

def captureJPEG(width, height):
    
    camera = picamera.PiCamera()
    imageData = StringIO.StringIO()
    w = int(width)
    h = int(height)

    try:
        camera.capture(imageData, format = "jpeg", resize = (w, h))
        imageData.seek(0)
        data = imageData.getvalue()
        return data
    finally:
        camera.close()
    return None  # error

def saveData(data, filename):
   
    file = open(filename, "wb")
    file.write(data)
    file.close()

def captureAndSave(width, height, filename):
    
    data = captureJPEG(width, height)
    if data != None:
        saveData(data, filename)

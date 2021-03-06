import cv2
import numpy as np
import boto3
from time import sleep


cap = cv2.VideoCapture(0)


# Setup
scale_factor = .15
green = (0,255,0)
red = (0,0,255)
frame_thickness = 2
cap = cv2.VideoCapture(0)
rekognition = boto3.client('rekognition')

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width, channels = frame.shape

    # Convert frame to jpg
    small = cv2.resize(frame, (int(width * scale_factor), int(height * scale_factor)))
    ret, buf = cv2.imencode('.jpg', small)

    # Detect faces in jpg
    faces = rekognition.detect_faces(Image={'Bytes':buf.tobytes()}, Attributes=['ALL'])

    # Draw rectangle around faces
    for face in faces['FaceDetails']:
        smile = face['Smile']['Value']
        cv2.rectangle(frame,
                      (int(face['BoundingBox']['Left']*width),
                       int(face['BoundingBox']['Top']*height)),
                      (int((face['BoundingBox']['Left']+face['BoundingBox']['Width'])*width),
                       int((face['BoundingBox']['Top']+face['BoundingBox']['Height'])*height)),
                      green if smile else red, frame_thickness)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print("hello")
    ret, fileImg=cv2.imencode('.png',img)
    response = client.detect_labels(Image={'Bytes':fileImg.tobytes()})
    print('Detected labels for Camera Capture')    
    for label in response['Labels']:
      print (label['Name'] + ' : ' + str(label['Confidence']))
      sleep(5)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
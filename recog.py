import cv2
import numpy as np
import boto3
from time import sleep


cap = cv2.VideoCapture(0)

while 1:
   ret, img = cap.read()
   client=boto3.client('rekognition')

   print("hello")
   ret, fileImg=cv2.imencode('.png',img)
   response = client.detect_labels(Image={'Bytes':fileImg.tobytes()}, MaxLabels=7, MinConfidence=70)
   print('Detected labels for Camera Capture')    
   for label in response['Labels']:
       		print (label['Name'] + ' ' + str(label['Confidence']))

   sleep(2)

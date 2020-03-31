import time
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
 

vs = cv2.VideoCapture(0)
time.sleep(2.0)
timeCheck = time.time()

faceCascade = cv2.CascadeClassifier('/home/abhishek/Desktop/Detection_opencv/faces.xml')

id=input('enter user id')
sampleNum=0
 
while(True):
    ret, frame = vs.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.2,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        sampleNum=sampleNum+1
        cv2.imwrite("/home/abhishek/Desktop/Detection_opencv/dataset/User."+id +'.'+str(sampleNum)+ ".jpg", gray[y:y+h,x:x+w]) 
        cv2.imshow('frame',frame)
        #cv2.imshow('gray',gray)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>20:
        break
    #print(1/(time.time() - timeCheck)) 
    #timeCheck = time.time()
 
# Cleanup before exit.
cv2.destroyAllWindows()
vs.stop()

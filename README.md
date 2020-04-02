Detection_opencv


This code helps you to understand and detect faces using webcam.

The whole process for face detection using opencv can be divided in three major steps:-

STEP1: CREATING A DATA SET
       (Run dataset.py file)
       
- For creating a data set we firstly have to import the following

  cv2
  
  NumPy

  imutils

  from imutils.video import videostream
  
- Face cascade = cv2.cascade classifier is their for face judging and compare it with xml files.

- Then we put the ID No. and the webcam starts capturing the images.

- After this the continuous frame is stored in variable.

- Then the coloured picture is converted in black & white.

- After this for the detection of face & eye and the rectangle box is also made in which the face will occur. this is based on pixels, coordinates, length of width, BGR, Thickness.

- Then their is a cv2.imwrite which is used to save an image to any stored device.

- cv2.imshow is to display frames on windows.

- The data set will be taking only 20 samples per person.

STEP2: TRAINER
       (Run trainer.py file)

- Some libraries needed to be import such as

  os

  cv2

  NumPy

  from PIL import image

- Their is a LBPHFace recognizer used to train the date set that output training data.yml files.

- Path is where the data will be stored.

- The stored data is trained for the further steps of detection.

STEP3: MAIN DETECTION
       (Run mainDetection1.py file)

- Some libraries needed to be import such as

  io

  os

  cv2

  NumPy

  from imutils.video import video stream

  imutils

  from PIL import image

- Face detection = cv2.cascade classifier is for judging face and compare it with yml files.

- LBPHFace recognizer used to train the data set that output training data.yml files.

- Recognizer.read is for training the data to get the output of a face.

- Then the continuous frame stored in variable, coloured to black & whits is done and the rectangle is made which collect the data of face. It is based on pixels, coordinates, lenght of width, BGR, Thickness.

- Then the data is mentioned for each and every person as per our requirment

  NAME

  AGE

  GENDER

  NATIONALITY / ETHNICITY

- To increase the data we need to increase the variables.



NOTE:- THIS CODE CAN DONE ITS DESIRABLE FUNCTIONING FOR A LARGE NO. OF PEOPLE. RIGHT NOW IT IS FOR 100 PEOPLE.

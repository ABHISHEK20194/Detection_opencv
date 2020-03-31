import time
import io

import cv2,os
import numpy
from imutils.video import VideoStream
import imutils
from PIL import Image

faceDetection=cv2.CascadeClassifier('/home/abhishek/Desktop/Detection_opencv/faces.xml')

 
vs = cv2.VideoCapture(0)
time.sleep(2.0)
timeCheck = time.time()

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/abhishek/Desktop/Detection_opencv/trainer/trainingData.yml')

id=0
gender=0
AGE=0
NATIONALITY=0
font=cv2.FONT_HERSHEY_SIMPLEX

while (True):
    ret, frame = vs.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceDetection.detectMultiScale(gray,1.1,5);
 
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])

        if(id == 1):
            id="AJAY DEVGAN"
            gender="MALE"
            AGE="50"
            NATIONALITY="INDIAN"
        elif(id == 2):
            id="HRITIK ROSHAN"
            gender="MALE"
            AGE="46"
            NATIONALITY="INDIAN"
        elif(id == 3):
            id="RANVEER SINGH"
            gender="MALE"
            AGE="34"
            NATIONALITY="INDIAN"
        elif(id == 4):
            id="AKSHAY KUMAR"
            gender="MALE"
            AGE="52"
            NATIONALITY="CANADIAN"
        elif(id == 5):
            id="SHAHID KAPOOR"
            gender="MALE"
            AGE="39"
            NATIONALITY="INDIAN"
        elif(id == 6):
            id="ADITI RAO HYDARI"
            gender="FEMALE"
            AGE="33"
            NATIONALITY="INDIAN"
        elif(id == 7):
            id="DISHA PATANI"
            gender="FEMALE"
            AGE="27"
            NATIONALITY="INDIAN"
        elif(id == 8):
            id="JACQUELINE FERNANDEZ"
            gender="FEMALE"
            AGE="34"
            NATIONALITY="SRI LANKAN"
        elif(id == 9):
            id="KIARA ADVANI"
            gender="FEMALE"
            AGE="27"
            NATIONALITY="INDIAN"
        elif(id == 10):
            id="NARGIS FAKHRI"
            gender="FEMALE"
            AGE="40"
            NATIONALITY="AMERICAN"
        elif(id == 11):
            id="TOM CRUISE"
            gender="MALE"
            AGE="57"
            NATIONALITY="AMERICAN"
        elif(id == 12):
            id="ROBERT DOWNEY JR."
            gender="MALE"
            AGE="54"
            NATIONALITY="AMERICAN"
        elif(id == 13):
            id="JOHNNY DEPP"
            gender="MALE"
            AGE="56"
            NATIONALITY="AMERICAN"
        elif(id == 14):
            id="HUGH JACKMAN"
            gender="MALE"
            AGE="51"
            NATIONALITY="AUSTRAILAN"
        elif(id == 15):
            id="WILL SMITH"
            gender="MALE"
            AGE="51"
            NATIONALITY="AMERICAN"
        elif(id == 16):
            id="MARGOT ROBBIE"
            gender="FEMALE"
            AGE="29"
            NATIONALITY="AUSTRAILAN"
        elif(id == 17):
            id="EMMA STONE"
            gender="FEMALE"
            AGE="31"
            NATIONALITY="AMERICAN"
        elif(id == 18):
            id="MILA KUNIS"
            gender="FEMALE"
            AGE="36"
            NATIONALITY="UKRAINIAN"
        elif(id == 19):
            id="EMMA WATSON"
            gender="FEMALE"
            AGE="29"
            NATIONALITY="BRITISH"
        elif(id == 20):
            id="SCARLETT JOHANSSON"
            gender="FEMALE"
            AGE="35"
            NATIONALITY="AMERICAN"
        elif(id == 21):
            id="AMIT SHAH"
            gender="MALE"
            AGE="55"
            NATIONALITY="INDIAN"
        elif(id == 22):
            id="ARVIND KEjRIWAL"
            gender="MALE"
            AGE="51"
            NATIONALITY="INDIAN"
        elif(id == 23):
            id="BARAK OBAMA"
            gender="MALE"
            AGE="58"
            NATIONALITY="AMERICAN"
        elif(id == 24):
            id="GEORGE W. BUSH"
            gender="MALE"
            AGE="73"
            NATIONALITY="AMERICAN"
        elif(id == 25):
            id="HILLARY RODHAM CLINTON"
            gender="FEMALE"
            AGE="72"
            NATIONALITY="AMERICAN"
        elif(id == 26):
            id="LALU PRASAD YADAV"
            gender="MALE"
            AGE="71"
            NATIONALITY="INDIAN"
        elif(id == 27):
            id="MAMTA BANERJEE"
            gender="FEMALE"
            AGE="65"
            NATIONALITY="INDIAN"
        elif(id == 28):
            id="MANMOHAN SINGH"
            gender="MALE"
            AGE="87"
            NATIONALITY="INDIAN"
        elif(id == 29):
            id="MAYAWATI"
            gender="FEMALE"
            AGE="64"
            NATIONALITY="INDIAN"
        elif(id == 30):
            id="NARENDRA MODI"
            gender="MALE"
            AGE="69"
            NATIONALITY="INDIAN"
        elif(id == 31):
            id="PRIYANKA GANDHI"
            gender="FEMALE"
            AGE="48"
            NATIONALITY="INDIAN"
        elif(id == 32):
            id="RAHUL GANDHI"
            gender="MALE"
            AGE="49"
            NATIONALITY="INDIAN"
        elif(id == 33):
            id="SONIA GANDHI"
            gender="FEMALE"
            AGE="73"
            NATIONALITY="INDIAN"
        elif(id == 34):
            id="YOGI ADITYANATH"
            gender="MALE"
            AGE="47"
            NATIONALITY="INDIAN"
        elif(id == 35):
            id="XI JINPING"
            gender="MALE"
            AGE="66"
            NATIONALITY="CHINESE"
        elif(id == 36):
            id="EMMANUEL MACRON"
            gender="MALE"
            AGE="42"
            NATIONALITY="FRENCH"
        elif(id == 37):
            id="VLADIMIR PUTIN"
            gender="MALE"
            AGE="67"
            NATIONALITY="RUSSIAN"
        elif(id == 38):
            id="BORIS JOHNSON"
            gender="MALE"
            AGE="55"
            NATIONALITY="BRITISH"
        elif(id == 39):
            id="SCOTT MORRISON"
            gender="MALE"
            AGE="51"
            NATIONALITY="AUSTRALIAN"
        elif(id == 40):
            id="CHRIS GAYLE"
            gender="MALE"
            AGE="40"
            NATIONALITY="JAMAICAN"
        elif(id == 41):
            id="CONOR MCGREGOR"
            gender="MALE"
            AGE="31"
            NATIONALITY="IRISH"
        elif(id == 42):
            id="CRISTIANO RONALDO"
            gender="MALE"
            AGE="35"
            NATIONALITY="PORTUGUESE"
        elif(id == 43):
            id="DAVID BECKHAM"
            gender="MALE"
            AGE="44"
            NATIONALITY="ENGLISH"
        elif(id == 44):
            id="KOBE BRYANT"
            gender="MALE"
            AGE="42"
            NATIONALITY="AMERICAN"
        elif(id == 45):
            id="LIONEL MESSI"
            gender="MALE"
            AGE="32"
            NATIONALITY="ARGENTINE"
        elif(id == 46):
            id="NEYMAR"
            gender="MALE"
            AGE="28"
            NATIONALITY="BRAZILIAN"
        elif(id == 47):
            id="MS DHONI"
            gender="MALE"
            AGE="38"
            NATIONALITY="INDIAN"
        elif(id == 48):
            id="RAFAEL NADAL"
            gender="MALE"
            AGE="33"
            NATIONALITY="SPANISH"
        elif(id == 49):
            id="RAHUL DRAVID"
            gender="MALE"
            AGE="47"
            NATIONALITY="INDIAN"
        elif(id == 50):
            id="ROGER FEDERER"
            gender="MALE"
            AGE="38"
            NATIONALITY="SWISS"
        elif(id == 51):
            id="SACHIN TENDULKAR"
            gender="MALE"
            AGE="46"
            NATIONALITY="INDIAN"
        elif(id == 52):
            id="VIRAT KHOLI"
            gender="MALE"
            AGE="31"
            NATIONALITY="INDIAN"
        elif(id == 53):
            id="VIRANDER SEHWAG"
            gender="MALE"
            AGE="41"
            NATIONALITY="INDIAN"
        elif(id == 54):
            id="ZLATAN IBRAHIMOVIC"
            gender="MALE"
            AGE="38"
            NATIONALITY="SWEDISH"
        elif(id == 55):
            id="APURVI CHANDELA"
            gender="FEMALE"
            AGE="27"
            NATIONALITY="INDIAN"
        elif(id == 56):
            id="DUTEE CHAND"
            gender="FEMALE"
            AGE="27"
            NATIONALITY="INDIAN"
        elif(id == 57):
            id="GEETA PHOGAT"
            gender="FEMALE"
            AGE="31"
            NATIONALITY="INDIAN"
        elif(id == 58):
            id="HEENA SIDHU"
            gender="FEMALE"
            AGE="30"
            NATIONALITY="INDIAN"
        elif(id == 59):
            id="MANIKA BATRA"
            gender="FEMALE"
            AGE="24"
            NATIONALITY="INDIAN"
        elif(id == 60):
            id="MARY KOM"
            gender="FEMALE"
            AGE="37"
            NATIONALITY="INDIAN"
        elif(id == 61):
            id="SAINA NEHWAL"
            gender="FEMALE"
            AGE="30"
            NATIONALITY="INDIAN"
        elif(id == 62):
            id="SAKSHI MALIK"
            gender="FEMALE"
            AGE="27"
            NATIONALITY="INDIAN"
        elif(id == 63):
            id="SANIA MIRZA"
            gender="FEMALE"
            AGE="33"
            NATIONALITY="INDIAN"
        elif(id == 64):
            id="TANIA SACHDEV"
            gender="FEMALE"
            AGE="33"
            NATIONALITY="INDIAN"
        elif(id == 65):
            id="JENNIFER LAWRENCE"
            gender="FEMALE"
            AGE="29"
            NATIONALITY="AMERICAN"
        elif(id == 66):
            id="ANGELINA JOLIE"
            gender="FEMALE"
            AGE="44"
            NATIONALITY="AMERICAN"
        elif(id == 67):
            id="JENNIFER ANISTON"
            gender="FEMALE"
            AGE="51"
            NATIONALITY="AMERICAN"
        elif(id == 68):
            id="ANNE HATHWAY"
            gender="FEMALE"
            AGE="37"
            NATIONALITY="AMERICAN"
        elif(id == 69):
            id="GAL GADOT"
            gender="FEMALE"
            AGE="34"
            NATIONALITY="ISRAELI"
        elif(id == 70):
            id="MEGAN FOX"
            gender="FEMALE"
            AGE="33"
            NATIONALITY="AMERICAN"
        elif(id == 71):
            id="ALEXANDRA DADDARIO"
            gender="FEMALE"
            AGE="34"
            NATIONALITY="AMERICAN"
        elif(id == 72):
            id="CHLOE GRACE MORETEZ"
            gender="FEMALE"
            AGE="23"
            NATIONALITY="AMERICAN"
        elif(id == 73):
            id="LILY COLLINS"
            gender="FEMALE"
            AGE="31"
            NATIONALITY="BRITISH"
        elif(id == 74):
            id="ANNA KENDRICK"
            gender="FEMALE"
            AGE="34"
            NATIONALITY="AMERICAN"
        elif(id == 75):
            id="BRAD PITT"
            gender="MALE"
            AGE="56"
            NATIONALITY="AMERICAN"
        elif(id == 76):
            id="CHRIS HEMSWORTH"
            gender="MALE"
            AGE="36"
            NATIONALITY="AUSTRALIAN"
        elif(id == 77):
            id="DWAYNE JOHNSON"
            gender="MALE"
            AGE="47"
            NATIONALITY="CANADIAN"
        elif(id == 78):
            id="KEANU REEVES"
            gender="MALE"
            AGE="55"
            NATIONALITY="CANADIAN"
        elif(id == 79):
            id="RYAN REYNOLDS"
            gender="MALE"
            AGE="43"
            NATIONALITY="CANADIAN"
        elif(id == 80):
            id="TOM HARDY"
            gender="MALE"
            AGE="42"
            NATIONALITY="BRITISH"
        elif(id == 81):
            id="ZAC EFRON"
            gender="MALE"
            AGE="32"
            NATIONALITY="AMERICAN"
        elif(id == 82):
            id="JOAQUIN PHOENIX"
            gender="MALE"
            AGE="45"
            NATIONALITY="AMERICAN"
        elif(id == 83):
            id="JASON STATHAM"
            gender="MALE"
            AGE="52"
            NATIONALITY="BRITISH"
        elif(id == 84):
            id="VARUN DHAWAN"
            gender="MALE"
            AGE="32"
            NATIONALITY="INDIAN"
        elif(id == 85):
            id="SANJAY DUTT"
            gender="MALE"
            AGE="60"
            NATIONALITY="INDIAN"
        elif(id == 86):
            id="RANBIR KAPOOR"
            gender="MALE"
            AGE="37"
            NATIONALITY="INDIAN"
        elif(id == 87):
            id="FARAHAN AKHTAR"
            gender="MALE"
            AGE="46"
            NATIONALITY="INDIAN"
        elif(id == 88):
            id="IRRFAN KHAN"
            gender="MALE"
            AGE="53"
            NATIONALITY="INDIAN"
        elif(id == 89):
            id="ABHISHEK BACHCHAN"
            gender="MALE"
            AGE="44"
            NATIONALITY="INDIAN"
        elif(id == 90):
            id="AMITABH BACHCHAN"
            gender="MALE"
            AGE="77"
            NATIONALITY="BRITISH RAJ"
        elif(id == 91):
            id="AMIR KHAN"
            gender="MALE"
            AGE="55"
            NATIONALITY="INDIAN"
        elif(id == 92):
            id="SALMAN KHAN"
            gender="MALE"
            AGE="54"
            NATIONALITY="INDIAN"
        elif(id == 93):
            id="SHAHRUKH KHAN"
            gender="MALE"
            AGE="54"
            NATIONALITY="INDIAN"
        elif(id == 94):
            id="ALIA BHATT"
            gender="FEMALE"
            AGE="27"
            NATIONALITY="BRITISH"
        elif(id == 95):
            id="BHUMI PEDNEKAR"
            gender="FEMALE"
            AGE="30"
            NATIONALITY="INDIAN"
        elif(id == 96):
            id="DIA MIRZA"
            gender="FEMALE"
            AGE="38"
            NATIONALITY="INDIAN"
        elif(id == 97):
            id="DIANA PENTY"
            gender="FEMALE"
            AGE="34"
            NATIONALITY="INDIAN"
        elif(id == 98):
            id="EVELYN SHARMA"
            gender="FEMALE"
            AGE="33"
            NATIONALITY="GERMAN"
        elif(id == 99):
            id="ELLI AVRAM"
            gender="FEMALE"
            AGE="29"
            NATIONALITY="SWEDISH"
        elif(id == 100):
            id="CHITRANGADA SINGH"
            gender="FEMALE"
            AGE="43"
            NATIONALITY="INDIAN"
        else:
            id="UNKNOWN"
        cv2.putText(frame,id,(x,y+h+20),font,1.0,(255,255,0));
        cv2.putText(frame,gender,(x,y+h+50),font,1.0,(0,255,255));
        cv2.putText(frame,AGE,(x,y+h+80),font,1.0,(255,0,255));
        cv2.putText(frame,NATIONALITY,(x,y),font,1.0,(0,255,0));

    cv2.imshow("face",frame);
    if(cv2.waitKey(1)==ord('q')):
        break;

cv2.destroyAllWindows()
vs.stop()

import cv2
import numpy as np
def facerecg(a):
    image = cv2.imread(a)
    output = np.copy(image)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces=faceCascade.detectMultiScale(output,1.3,5)
    for (x,y,w,h) in faces:
        p=13
        output = cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),2)
        roi_image = image[y-p:y+h+p, x-p:x+w+p]
    cv2.imshow('face recogonition',output)
    cv2.waitKey()
    cv2.destroyAllWindows()
s=(input('enter path of the image:'))
facerecg(s)
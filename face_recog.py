import cv2
import numpy as np
import face_recognition

shin = face_recognition.load_image_file('./img/faces/shin.JPG')
shin = cv2.cvtColor(shin, cv2.COLOR_BGR2RGB)

bohr = face_recognition.load_image_file('./img/faces/bohr1.JPG')
bohr = cv2.cvtColor(bohr, cv2.COLOR_BGR2RGB)

bohr_test = face_recognition.load_image_file('./img/faces/bohr2.JPG')
bohr_test = cv2.cvtColor(bohr_test, cv2.COLOR_BGR2RGB)

faceLocshin = face_recognition.face_locations(shin)[0]
encodeshin = face_recognition.face_encodings(shin)[0]
cv2.rectangle(shin, (faceLocshin[3], faceLocshin[0]), (faceLocshin[1], faceLocshin[2]), (255, 0, 255), 2)

faceLocbohr = face_recognition.face_locations(bohr)[0]
encodebohr = face_recognition.face_encodings(bohr)[0]
cv2.rectangle(bohr, (faceLocbohr[3], faceLocbohr[0]), (faceLocbohr[1], faceLocbohr[2]), (255, 0, 255), 2)

faceLoctest = face_recognition.face_locations(bohr_test)[0]
encodebohrtest = face_recognition.face_encodings(bohr_test)[0]
cv2.rectangle(bohr_test, (faceLoctest[3], faceLoctest[0]), (faceLoctest[1], faceLoctest[2]), (255, 0, 255), 2)

results1 = face_recognition.compare_faces([encodebohr], encodebohrtest)
results2 = face_recognition.compare_faces([encodebohr], encodeshin)

faceDis1 = face_recognition.face_distance([encodebohr], encodebohrtest)
faceDis2 = face_recognition.face_distance([encodebohr], encodeshin)

print('보어 + 보어 테스트 : %s (%f%%)' %(results1, 1-faceDis1))
print('보어 + 신해철 테스트 : %s (%f%%)' %(results2, 1-faceDis2))

# cv2.imshow('shin', shin)
# cv2.imshow('bohr', bohr)
# cv2.waitKey(0)
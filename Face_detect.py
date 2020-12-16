import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/seonghee.choi/Anaconda3/envs/ImgProcessing/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/seonghee.choi/Anaconda3/envs/ImgProcessing/Lib/site-packages/cv2/data/haarcascade_eye.xml')
#
src = cv2.imread('./img/shin.JPG')

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray,2.2,3) #1.1: scale factor 로 얼굴이나 눈등 지정한 형태를 찾을 정밀도 의미, 3 : MinNeighbors로 얼굴 사이의 최소 간격
#
for x, y, w, h in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face = src[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#
# cv2.imwrite('C:/Users/Administrator/Desktop/python/origin/face_cascade.jpg', src)
cv2.imshow('Bohr', src)
cv2.waitKey(0)
cv2.destroyAllWindows()
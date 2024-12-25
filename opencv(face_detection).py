# face detection by image
import cv2
img = cv2.imread("my_image.jpg")
face_dector = cv2.CascadeClassifier("detect_face.xml")
faces = face_dector.detectMultiScale(img, scaleFactor = 1.4, minNeighbors = 3, minSize = (10, 10))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (w+x, h+y), (4, 255, 80), 4)
cv2.imshow("Image", img)
cv2.waitKey(0)





# face detection by webcam
import cv2
import time
capture = cv2.VideoCapture(0)
while True:
    is_Ture, framex = capture.read()
    face_dector = cv2.CascadeClassifier("detect_face.xml")
    faces = face_dector.detectMultiScale(framex, scaleFactor = 1.4, minNeighbors = 3, minSize = (10, 10))
    for (x, y, w, h) in faces:
        cv2.rectangle(framex, (x, y), (w+x, h+y), (4, 255, 80), 4)
    cv2.imshow("my video", framex)
    if cv2.waitKey(20) & 0xff == ord("x"):
        break

# if you want to make project for opencv get files from opencv github profile files like (detect_face.xml)
# https://github.com/opencv/opencv/tree/4.x/data/haarcascades
# Displaying Video Capture from Webcam
import cv2
cap = cv2.VideoCapture(0)
while True:
  ret, frame = cap.read()
  cv2.imshow('Webcam', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
#Display video
import cv2
import time
capture = cv2.VideoCapture("anime.mp4")
while True:
    x, y = capture.read()
    time.sleep(0)
    cv2.imshow("my video", y)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
# save video 
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
  ret, frame = cap.read()
  out.write(frame)

  cv2.imshow('Webcam', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

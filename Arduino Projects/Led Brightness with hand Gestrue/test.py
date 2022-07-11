import cv2

cap= cv2.VideoCapture(1)

while True:
    succ, img = cap.read()
    cv2.imshow("Im",img)
    cv2.waitKey(1)
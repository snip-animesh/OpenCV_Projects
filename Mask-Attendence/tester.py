import cv2 as cv
import warnings
warnings.filterwarnings('ignore')
import detect_mask,conAttendence
import keyboard

cap=cv.VideoCapture(0)

while True:
    success,img=cap.read()
    detect_mask.main(img)
    k=cv.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
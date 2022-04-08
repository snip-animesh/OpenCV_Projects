import cv2 as cv

cap=cv.VideoCapture(0)
faceDetect=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
count=0
while True:
    success,img=cap.read()
    # pc camera gives mirror image , that's why flip it.
    img=cv.flip(img,1)
    faces=faceDetect.detectMultiScale(img,1.3,5)
    for x,y,w,h in faces:
        count+=1
        name='./Images/Face Without Mask/' + str(count) + ".jpg"
        print("Creating.."+name)
        cv.imwrite(name,img[y:y+h,x:x+h])
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv.imshow("Webcam",img)
    k=cv.waitKey(1)
    if count>499:
        break
cap.release()
cv.destroyAllWindows()
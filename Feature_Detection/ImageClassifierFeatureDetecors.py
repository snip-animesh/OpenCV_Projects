import cv2
import numpy as np
import os

# img1=cv2.imread("ImageQuery/ps4fifa.jpg",0)
# img2=cv2.imread("ImageQuery/ps4fifa2.jpg",0)
#
# orb=cv2.ORB_create(nfeatures=1000)
#
# kp1,des1=orb.detectAndCompute(img1,None)
# kp2,des2=orb.detectAndCompute(img2,None)

# imgKp1=cv2.drawKeypoints(img1,kp1,None)
# imgKp2=cv2.drawKeypoints(img2,kp1,None)

# bf=cv2.BFMatcher()
# matches=bf.knnMatch(des1,des2,k=2)
#
# good=[]
# for m,n in matches:
#     if m.distance <0.75* n.distance:
#         good.append([m])
#
# print(len(good))
#
# img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
#
# cv2.imshow("Image1",img1)
# cv2.imshow("Image2",img2)
# cv2.imshow("Image3",img3)

# cv2.imshow("ImageKp1",imgKp1)
# cv2.imshow("ImageKp2",imgKp2)

PATH = 'ImageQuery'
ORB = cv2.ORB_create(nfeatures=1000)

######### Importing Images ########
images = []
classNames = []
myList = os.listdir(PATH)

print("Total classes detected ", len(myList))

for cl in myList:
    imgCur = cv2.imread(f'{PATH}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)


# Finding keyPoints and descriptor from all images
def findDes(images):
    desLst = []
    for img in images:
        kp, des = ORB.detectAndCompute(img, None)
        desLst.append(des)
    return desLst


desLst = findDes(images)
print(len(desLst))


def findIDs(img, desLst, thres=15):
    kp2, des2 = ORB.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchLst = []
    finalValue = -1

    try:
        for des in desLst:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchLst.append(len(good))
        # print(matchLst)
    except:
        pass
    if len(matchLst) != 0 and max(matchLst) > thres:
        finalValue = matchLst.index(max(matchLst))
    return finalValue


cap = cv2.VideoCapture(0)

while True:
    success, img2 = cap.read()
    imgOrginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findIDs(img2, desLst)
    if id !=-1:
        cv2.putText(imgOrginal,classNames[id],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    cv2.imshow("WebCam", imgOrginal)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

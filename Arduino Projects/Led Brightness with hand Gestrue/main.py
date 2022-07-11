import cv2
import time
import math
import HandTrackingModule as htm

pTime = 0

detector = htm.HandDetector(minDectionCon=0.7)


def run(img):
    global pTime
    length = None
    # detect hand
    img = detector.findHands(img, draw=False)

    lmList = detector.findPosition(img, draw=False)  # get positions
    if len(lmList):
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # getting midpoint of two points

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)  # drawing a line between the points
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x1 - x2, y1 - y2)  # finding length between two point
        # print(length)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0),
                       cv2.FILLED)  # when length is less than 50 , make it green . it will give button effect

    cTime = time.time()
    fps = 1 / (cTime - pTime)

    cv2.putText(img, f'Fps:{int(fps)}', (20, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    return length


if __name__ == "__main__":
    # Camera height and width
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    while True:
        succ, img = cap.read()
        length = run(img)
        if length != None:
            print(length)


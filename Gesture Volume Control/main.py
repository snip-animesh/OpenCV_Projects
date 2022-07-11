import cv2
import time
import numpy as np
import mediapipe as mp
import math
import HandTrackingModule as htm

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Camera height and width
wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.HandDetector(minDectionCon=0.7)

####################
# PYCAW CODE
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
#####################

minVol = volRange[0]
maxVol = volRange[1]
# print(minVol, maxVol)

vol = 0
volBar=400
volPercentage=0

while True:
    succ, img = cap.read()

    # detect hand
    img = detector.findHands(img, draw=True)

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

        # Hand Range 22 to 220
        # volume range -74 to 0

        vol = np.interp(length, [22, 220], [minVol, maxVol])
        volBar = np.interp(length, [22, 220], [400,150])
        volPercentage = np.interp(length, [22, 220], [0,100])
        volume.SetMasterVolumeLevel(vol, None)
        # print(vol)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0),
                       cv2.FILLED)  # when length is less than 50 , make it green . it will give button effect

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'Fps:{int(fps)}', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, f'{int(volPercentage)}%', (40, 140), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

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

detector = htm.HandDetector(minDectionCon=0.7, maxHands=1)

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
volBar = 400
volPercentage = 0
area = 0
colorVol =(209, 202, 156)

while True:
    succ, img = cap.read()

    # Find hand
    img = detector.findHands(img, draw=True)

    lmList, bbox = detector.findPosition(img, draw=True)  # get positions
    if len(lmList):
        # Filter Based on size
        area = ((bbox[2] - bbox[0]) * (bbox[3] - bbox[1])) // 100
        # print(area)
        if 200 < area < 700:
            # print("Yes")
            # Find Distance between index and Thumb
            length, img, line_info = detector.findDistance(4, 8, img)
            # print(length)
            #########Convert Volume #####

            # Hand Range 22 to 220
            # volume range -74 to 0
            volBar = np.interp(length, [22, 200], [400, 150])
            volPercentage = np.interp(length, [22, 200], [0, 100])

            # Reduce Resolution to maki it smoother
            smoothness = 2
            volPercentage = smoothness * round(volPercentage / smoothness)

            # Check fingers up
            fingers = detector.fingersUp()
            print(fingers)
            # If pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPercentage / 100, None)
                cv2.circle(img, (line_info[4], line_info[5]), 10, (0, 255, 0),
                           cv2.FILLED)  # when pinky finger is down , make it green . it will give button effect
                colorVol=(219,106,30)
            else:
                colorVol = (209, 202, 156)

    # Drawings
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cVol = int(volume.GetMasterVolumeLevelScalar()*100)
    cv2.putText(img, f'Vol Set:{int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, colorVol, 2)

    # Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'Fps:{int(fps)}', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, f'{int(volPercentage)}%', (40, 140), cv2.FONT_HERSHEY_COMPLEX, 1, (234,212,70), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

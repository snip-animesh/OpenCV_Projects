import cv2 as cv
import mediapipe as mp
import controllerOwn as ctn

videoCapture = cv.VideoCapture(1)
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

# use right hand
with mp_hand.Hands(max_num_hands=1) as hands:
    while True:
        success, img = videoCapture.read()
        img = cv.flip(img, 1)
        image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        lmList = []

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape  # height, weight, coordinate
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id,lm.x,lm.y)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers = []
        if len(lmList) != 0:
            # For thumb
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            #      for other fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            ctn.led(fingers)

        cv.imshow("WebCam", image)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
ctn.led([0, 0, 0, 0, 0])
videoCapture.release()
cv.destroyAllWindows()

# My own code !!

import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1, minDectionCon=0.5, trackingConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.DetectionCon = minDectionCon
        self.trackCon = trackingConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.DetectionCon,
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        # print(result.multi_hand_landmarks)

        if self.result.multi_hand_landmarks:
            for handLmarks in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLmarks, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=0):
        lmList = []

        if self.result.multi_hand_landmarks:

            myHand = self.result.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)  # position of center
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cap = cv2.VideoCapture(1)

    detector = HandDetector()

    while True:
        succ, img = cap.read()

        img = detector.findHands(img)

        lmList = detector.findPosition(img)
        try:
            print(lmList[4])
        except:
            pass
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

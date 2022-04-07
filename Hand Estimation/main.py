import cv2 as cv
import mediapipe as mp

videoCapture = cv.VideoCapture(0)
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
with mp_hand.Hands() as hands:
    while True:
        success, img = videoCapture.read()
        image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        cv.imshow("WebCam", image)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
videoCapture.release()
cv.destroyAllWindows()

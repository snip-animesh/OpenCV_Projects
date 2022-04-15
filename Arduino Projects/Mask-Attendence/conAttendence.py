import cv2 as cv, face_recognition
import numpy as np, pickle
from datetime import datetime

DIR = r"D:\python Code\Attendence Project\dataset_faces.dat"
with open(DIR, 'rb') as f:
    encodeKnown = pickle.load(f)
print("Got Encodings !! ")
classNames = list(encodeKnown.keys())
encodeKnown = np.array(list(encodeKnown.values()))


def getAttendence(name, roll):
    with open('conAttendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{roll},{dtString}')


def main_attendence(img_at):
    imgS = cv.cvtColor(img_at, cv.COLOR_BGR2RGB)
    # cv.imshow("Detected Face", img_at)

    # detect face
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        # find matching
        matches = face_recognition.compare_faces(encodeKnown, encodeFace)
        # find distance
        faceDis = face_recognition.face_distance(encodeKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            nameRoll = classNames[matchIndex].upper()
            name, roll = nameRoll.split('_')
            y1, x2, y2, x1 = faceLoc
            cv.rectangle(img_at, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv.rectangle(img_at, (x1, y2), (x2 + 10, y2 + 40), (0, 255, 0), cv.FILLED)
            cv.putText(img_at, name, (x1 + 2, y2 + 28), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # cv.imshow("Detected Face", img_at)
            getAttendence(name, roll)
            return name,roll

import cv2
import pytesseract
import TrieAlg
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
FolderPath = r'D:\python Code\OpenCV projects\Text to word\Resources\Snaps'
VideoLocation = ""

finder = TrieAlg.Trie()


class SnapToAttendence:
    def __init__(self):
        self.Roll_time = []

    def detecting_words(self, img, putText=True):
        hImg, wImg, _ = img.shape
        boxes = pytesseract.image_to_data(img)  # Returns left bottom right top (diagonal points)
        splitted_boxes = boxes.splitlines()
        # print(splitted_boxes[2].split()[-2])

        for counter, b in enumerate(boxes.splitlines()):
            if counter == 0:
                continue
            b = b.split()
            # print(b)

            # detect roll and entry time
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)  # here they did proper formatting
                if putText:
                    cv2.putText(img, b[-1], (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

                # The sender's roll num is 4 words before the word "AM"
                # execute print(b) if don't understand

                if b[-1] == "AM" or b[-1] == "PM":
                    roll = splitted_boxes[counter - 4].split()[-1]
                    self.Roll_time.append((roll, (splitted_boxes[counter - 1].split()[-1]) + " " + b[-1]))

        return img, self.Roll_time

    def csv_maker(self, Roll_time):
        with open("Resources/attendence.csv", 'r+') as fp:
            prevDatas=fp.readlines()  # Previous lines in csv file deletes without this command

            # To prevent duplicate in csv file
            for line in prevDatas:
                entry=line.split(',')
                finder.insert(entry[0])

            for roll, time in Roll_time:
                if not finder.search(roll):
                    finder.insert(roll)
                    fp.writelines(f'\n{roll},{time}')
        fp.close()


# To get all images in the given directory
def finding_all_images(FolderPath):
    ImageList = os.listdir(FolderPath)
    return ImageList


snapToAttendence = SnapToAttendence()


# Run the programm using picture in 'FolderPath' folder
def main_for_images():
    ImageList = finding_all_images(FolderPath)
    for image in ImageList:
        img = cv2.imread(f'{FolderPath}/{image}')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img, Roll_time = snapToAttendence.detecting_words(img, putText=False)

        snapToAttendence.csv_maker(Roll_time)
        print(Roll_time)

        finding_all_images(FolderPath)
        cv2.imshow("Result", img)
        cv2.waitKey(2000)


def main_for_video():
    cap = cv2.imread(VideoLocation)
    while True:
        succ, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img, Roll_time = snapToAttendence.detecting_words(img, putText=False)

        snapToAttendence.csv_maker(Roll_time)
        print(Roll_time)

        finding_all_images(FolderPath)
        cv2.imshow("Result", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main_for_images()
    # main_for_video()

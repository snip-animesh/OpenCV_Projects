import cv2
import pytesseract
import TrieAlg

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

finder = TrieAlg.Trie()


class SnapToAttendence:
    def __init__(self):
        self.Roll_time=[]

    def detecting_words(self,img, putText=True):
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
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # here they did proper formatting
                if putText:
                    cv2.putText(img, b[-1], (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

                # The sender's roll num is 4 words before the word "AM"
                # execute print(b) if don't understand

                if b[-1] == "AM" or b[-1] == "PM":
                    roll = splitted_boxes[counter - 4].split()[-1]
                    if not finder.search(roll):
                        finder.insert(roll)
                        self.Roll_time.append((roll, (splitted_boxes[counter - 1].split()[-1]) + " " + b[-1]))

        print(self.Roll_time)
        return img


snapToAttendence=SnapToAttendence()

if __name__ == "__main__":
    img = cv2.imread('Resources/1.JPG')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = snapToAttendence.detecting_words(img, putText=False)

    cv2.imshow("Result", img)
    cv2.waitKey(0)

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def detecting_characters(img, putText=True):
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)  # Returns left bottom right top (diagonal points)

    for b in boxes.splitlines():
        b = b.split()
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        # print(x, y, w, h)
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
        if putText:
            cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    return img


def detecting_words(img,putText=True):
    hImg, wImg, _ = img.shape
    # configurations=r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_data(img)  # Returns left bottom right top (diagonal points)
    # print(boxes)

    for x, b in enumerate(boxes.splitlines()):
        if x == 0:
            continue
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # here they did proper formatting
            if putText:
                cv2.putText(img, b[-1], (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    return img


def detecting_digits(img,putText=True):
    hImg, wImg, _ = img.shape
    configurations = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_data(img, config=configurations)  # Returns left bottom right top (diagonal points)
    # print(boxes)

    for x, b in enumerate(boxes.splitlines()):
        if x == 0:
            continue
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # here they did proper formatting
            if putText:
                cv2.putText(img, b[-1], (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    return img


if __name__ == "__main__":
    img = cv2.imread('1.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(img))

    img = detecting_words(img)

    cv2.imshow("Result", img)
    cv2.waitKey(0)

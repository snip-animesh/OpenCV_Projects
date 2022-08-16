import easyocr
import cv2
from matplotlib import pyplot as plt

DIR=r'D:\python Code\OpenCV projects\Text to word\Resources\Snaps\1.JPG'
IMG=cv2.imread(DIR)
def ocrReading():
    image =IMG
    reader = easyocr.Reader(['en'])
    result = reader.readtext(DIR)

    for res in result:
        # print(res)
        # print(len(res[1]))
        if len(res[1]) == 19 :
            image=drawings(IMG,res[0][0],res[0][2])
    return image

# Drawing detected rolls
def drawings(img,point1, point2):
    cv2.rectangle(img,point1,point2,(255,0,0,1))
    return img


if __name__ == "__main__":
    image=ocrReading()
    plt.imshow(image)
    plt.show()
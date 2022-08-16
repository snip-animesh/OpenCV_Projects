import easyocr
import cv2
from matplotlib import pyplot as plt

DIR=r'D:\python Code\OpenCV projects\Text to word\Resources\Snaps\2.JPG'
img=cv2.imread(DIR)


reader = easyocr.Reader(['en'])
result = reader.readtext(DIR)
# print(result)
for res in result:
    if len(res[1]) == 20:
        cv2.rectangle(img,tuple(res[0][0]), tuple(res[0][2]), (0,255,0), 1)

plt.imshow(img)
plt.show()
import warnings
import matplotlib.pyplot as plt
import os
import cv2 as cv
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Activation, Dropout, Flatten

warnings.filterwarnings('ignore')

path = "images"
images = []
classNo = []
testRatio = 0.2
valRatio = 0.2
imgDimension = (32, 32, 3)

myList = os.listdir(path)
numOfClasses = len(myList)
# print(numOfClasses)

for x in range(0, numOfClasses):
    myPicList = os.listdir(path + "/" + str(x))
    for y in myPicList:
        curImg = cv.imread(path + "/" + str(x) + "/" + y)
        curImg = cv.resize(curImg, (imgDimension[0], imgDimension[1]))
        images.append(curImg)
        classNo.append(x)
    print(x)

images = np.array(images)
classNo = np.array(classNo)

x_train, x_test, y_train, y_test = train_test_split(images, classNo, test_size=testRatio)
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=testRatio)

numOfSample = []

for x in range(0, numOfClasses):
    numOfSample.append(len(np.where(y_train == x)[0]))

plt.figure(figsize=(10, 5))
plt.bar(range(0, numOfClasses), numOfSample)
plt.title("Bar Plot of Classes & Images")
plt.xlabel("No Of Classes")
plt.ylabel("No of Images")
plt.show()


def preprocessing(img):
    # img=np.astype("uint8")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)
    img = img / 255
    return img


x_train = np.array(list(map(preprocessing, x_train)))
x_test = np.array(list(map(preprocessing, x_test)))
x_validation = np.array(list(map(preprocessing, x_validation)))

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_validation = x_validation.reshape(x_validation.shape[0],
                                    x_validation.shape[1], x_validation.shape[2], 1)

dataGen = ImageDataGenerator(width_shift_range=0.1, height_shift_range=0.1, zoom_range=0.2,
                             shear_range=0.1, rotation_range=10)

dataGen.fit(x_train)

y_train = to_categorical(y_train, numOfClasses)
y_test = to_categorical(y_test, numOfClasses)
y_validation = to_categorical(y_validation, numOfClasses)


def myModel():
    sizeOfFilter1 = (3, 3)
    sizeOfFilter2 = (3, 3)
    sizeOfPool = (2, 2)

    model = Sequential()
    model.add((Conv2D(32, sizeOfFilter1,
                      input_shape=(imgDimension[0], imgDimension[1], 1), activation='relu')))
    model.add((Conv2D(32, sizeOfFilter1, activation='relu')))
    model.add(MaxPooling2D(pool_size=sizeOfPool))

    model.add((Conv2D(64, sizeOfFilter2, activation='relu')))
    model.add((Conv2D(64, sizeOfFilter2, activation='relu')))
    model.add(MaxPooling2D(pool_size=sizeOfPool))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(numOfClasses, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


model = myModel()
print(model.summary())

history=model.fit_generator(dataGen.flow(x_train, y_train,batch_size=50),
steps_per_epoch=1000,epochs=2,validation_data=(x_validation,y_validation),shuffle=1)

model.save("TrainedModel.h5")

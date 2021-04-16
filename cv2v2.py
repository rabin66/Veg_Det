from datetime import datetime

import cv2
import tensorflow as tf
import numpy as np
import pandas as pd

threshold = 0.85  # PROBABLITY THRESHOLD
font = cv2.FONT_HERSHEY_SIMPLEX
##############################################

# SETUP THE VIDEO CAMERA
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
model = tf.keras.models.load_model("CNN.model")
IMG_SIZE = 50

def preprocessing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img

def getClassName(classNo):
    if classNo == 0:
        return 'Tomato'
    elif classNo == 1:
        return 'Onion'
    elif classNo == 2:
        return 'Potato'
    else:
        return 'None'

def getClassPrice(classNo):
    todaydate = datetime.now()
    filename = todaydate.strftime("%Y%m%d" + ".csv")

    df = pd.read_csv(filename, usecols=[1, 5])

    tomato_price = df[df['Commodity'] == 'Tomato Big(Nepali)' ]['Average'].values
    potato_price = df[df['Commodity'] == 'Potato Red' ]['Average'].values
    onion_price = df[df['Commodity'] == 'Onion Dry (Indian)' ]['Average'].values

    if classNo == 0:
        return tomato_price
    elif classNo == 1:
        return potato_price
    elif classNo == 2:
        return onion_price
    elif classNo == 4:
        return 'None'

def camera_operate():
    while True:
        # READ IMAGE
        success, imgOriginal = cap.read()

        # PROCESS IMAGE
        img = np.asarray(imgOriginal)

        img = cv2.resize(img, (50, 50))
        # print(img.shape)
        img = preprocessing(img)
        img = img.reshape(1, 50, 50, 1)
        img = np.array(img).reshape(1, 50, 50, 1)
        cv2.putText(imgOriginal, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(imgOriginal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(imgOriginal, "PRICE: (in RS)", (20, 115), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        # PREDICT IMAGE
        classIndex = model.predict_classes(img)
        predictions = model.predict(img)
        probabilityValue = np.amax(predictions)
        print(getClassName(classIndex))
        print(classIndex, probabilityValue)
        if probabilityValue > threshold:
            cv2.putText(imgOriginal, str(classIndex) + " " + str(getClassName(classIndex)), (120, 35), font, 0.75,
                        (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(imgOriginal, str(round(probabilityValue * 100, 2)) + "%", (180, 75), font, 0.75, (0, 0, 255), 2,
                        cv2.LINE_AA)
            cv2.putText(imgOriginal, str(getClassPrice(classIndex)), (220, 115), font, 0.75,
                        (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("Original Image", imgOriginal)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return None
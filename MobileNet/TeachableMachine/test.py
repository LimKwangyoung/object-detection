import cv2
import numpy as np
from keras.models import load_model


# disable scientific notation
np.set_printoptions(suppress=True)

model = load_model('models/keras_model.h5', compile=False)
class_names = open('labels.txt', 'r').readlines()

# 0: rear camera, 1: front camera
camera = cv2.VideoCapture(1)

while True:
    ret, image = camera.read()

    if not ret:
        break

    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    cv2.imshow('Webcam Image', image_resized)

    image_array = (np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3) / 127.5) - 1
ㅁ
    # predict
    prediction = model.predict(image_array)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    print(f'Class: {class_name}, Confidence Score: {confidence_score:.2f}%')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

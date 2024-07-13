import cv2

# pretrained classes in the model
class_names = {
    0: 'background',
    1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
    7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
    13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
    18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
    24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
    32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
    37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
    41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
    46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
    51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
    56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
    61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
    67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
    75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
    80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
    86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'
}

# loading model
model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

try:
    while True:
        ret, frame = camera.read()

        if not ret:
            break

        # preprocessing
        image_height, image_width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True)

        # predict
        model.setInput(blob)
        output = model.forward()

        for detection in output[0, 0, :]:
            confidence = detection[2]
            if confidence > 0.5:
                class_id = int(detection[1])
                class_name = class_names.get(class_id, 'Unknown')

                box_x = int(detection[3] * image_width)
                box_y = int(detection[4] * image_height)
                box_width = int(detection[5] * image_width)
                box_height = int(detection[6] * image_height)

                print(f'Class: {class_name}, Confidence: {confidence:.2f}')

                cv2.rectangle(frame, (box_x, box_y), (box_width, box_height), (23, 230, 210), thickness=2)
                cv2.putText(frame, f'{class_name}: {confidence:.2f}', (box_x, box_y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print('Interrupted by user')
finally:
    camera.release()
    cv2.destroyAllWindows()

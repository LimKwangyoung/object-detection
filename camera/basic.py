import cv2

# 0: rear camera, 1: front camera
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

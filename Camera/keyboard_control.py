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
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('1'):
        pass
    elif key == ord('2'):
        pass
    elif key == ord('3'):
        pass
    elif key == ord('4'):
        pass

cap.release()
cv2.destroyAllWindows()

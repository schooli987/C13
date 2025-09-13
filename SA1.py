import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)  # wait for camera to initialize

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)


    cv2.imshow("Invisibility Cloak", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

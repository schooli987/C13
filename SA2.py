import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
time.sleep(2)  # wait for camera to initialize

print("Capturing background... please move out of frame!")
for i in range(60):   # take multiple frames for stability
    ret, background = cap.read()
    if not ret:
        continue
    background = cv2.flip(background, 1)

print("Background captured successfully!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color ranges
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create mask
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine the mask (remove noise)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    cv2.imshow("Invisibility Cloak", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

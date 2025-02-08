import cv2
import os

name = input("Enter the name to store face data: ")
save_path = f"face_data/{name}.jpg"

if not os.path.exists('face_data'):
    os.makedirs('face_data')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

ret, frame = cap.read()
if ret:
    cv2.imwrite(save_path, frame)
    print(f"Face data saved for {name} at {save_path}")
else:
    print("Failed to capture image.")

cap.release()

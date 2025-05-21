import cv2
import numpy as np
import os

# Path to your local XML file
cascade_path = 'haarcascade_car.xml'

# Check if the file exists
if not os.path.exists(cascade_path):
    print(f"❌ Error: File '{cascade_path}' not found.")
    print("👉 Download it from:")
    print("   https://github.com/andrewssobral/vehicle_detection_haarcascades/blob/master/haarcascade_car.xml")
    exit()

# Load pre-trained vehicle classifier
vehicle_cascade = cv2.CascadeClassifier(cascade_path)
if vehicle_cascade.empty():
    print("❌ Error: Could not load cascade classifier.")
    exit()

# Use the full absolute path to your video file here:
video_path = video_path = r"C:\Users\hp\OneDrive\Desktop\python\myvideo.mp4.mp4"


# Start video capture (0 = default webcam or use video path)
cap = cv2.VideoCapture(video_path)  # Use 0 for webcam

if not cap.isOpened():
    print(f"❌ Error: Could not open video file or webcam at '{video_path}'.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 2)

    # Reset vehicle count per frame
    vehicle_count = len(vehicles)

    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, f'Vehicle Count: {vehicle_count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Vehicle Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

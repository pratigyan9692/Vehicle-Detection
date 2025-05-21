# 🚗 Vehicle Detection using OpenCV and Haar Cascades

This Python project detects vehicles in a video using a pre-trained Haar Cascade classifier with OpenCV. It highlights detected vehicles in real-time and displays the vehicle count on each frame.

## 📂 Project Structure

vehicle_detection/
├── haarcascade_car.xml # Haar cascade XML file for vehicle detection
├── myvideo.mp4.mp4 # Input video file (replace with your own)
├── vehicle_detection.py # Main Python script

## ✅ Features

- Detects cars in real-time from a video file or webcam
- Draws bounding boxes around detected vehicles
- Displays vehicle count on each frame
- Lightweight and easy to use

## 🛠 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

Install dependencies using:

```bash
pip install opencv-python numpy
📥 Setup
Clone or download this repository.

Download the Haar Cascade XML file from:
haarcascade_car.xml
and place it in the same directory.

Replace the video_path variable with your own video file path (or set it to 0 for webcam).
▶️ How to Run
python vehicle_detection.py
Press Q to quit the window.

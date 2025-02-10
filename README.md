# Hand-Detection using OpenCV and Mediapipe
This project implements real-time hand detection using OpenCV and MediaPipe. It utilizes a webcam feed to detect hands and visualize their landmarks with connections.

Features
1. Real-time hand detection
2. Tracks up to two hands
3. Draws hand landmarks and connections
4. Uses OpenCV for image processing
5. Utilizes MediaPipe Hands module for robust hand tracking

Prerequisites
Ensure you have Python installed along with the following dependencies:
pip install opencv-python mediapipe

Usage
Clone the repository or copy the script.
Run the Python script:
python hand_detection.py
The webcam window will open, showing real-time hand tracking.
Press q to exit the application.

Code Explanation
Initializes OpenCV and MediaPipe Hands module.
Captures video frames from the webcam.
Converts frames to RGB for MediaPipe processing.
Detects hand landmarks and draws them on the frame.
Displays the processed frame in real-time.

Key Libraries Used
OpenCV: For video capture and image processing.
MediaPipe: For efficient hand detection and tracking.

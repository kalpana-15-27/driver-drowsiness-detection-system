# driver-drowsiness-detection-system
A real-time safety application built for the Microsoft Elevate Internship using Python 3.14 and OpenCV. It utilizes Haar Cascade classifiers to monitor driver fatigue and triggers an automated audio alarm within 0.5 seconds of detecting a microsleep event.

Microsoft Elevate AICTE Internship Project | Jan 20 - Feb 15, 2026

## Project Overview
This project is a real-time safety application designed to combat driver fatigue and prevent road accidents. Developed during a intensive 4-week internship, the system utilizes Computer Vision and Facial Landmark Detection to monitor driver alertness and provide an immediate audio-visual intervention when signs of drowsiness are detected.

## Key Features
Real-Time Monitoring: Captures live video at a stable 30 FPS to track facial expressions.

Dlib 68-Point Landmarks: Utilizes high-precision facial landmark detection to map specific ocular coordinates.

Intelligent Alert System: Triggers an automated alarm after 0.5 seconds (15 frames) of detected microsleep.

Audio-Visual Intervention: Immediate feedback provided via on-screen alerts and a low-latency audio alarm managed through Pygame.

## Required Assets
[!IMPORTANT]
Due to GitHub's 100MB file size limit, the required pre-trained model file must be downloaded externally.

#### File Name: shape_predictor_68_face_landmarks.dat

## Download Link:  [https://drive.google.com/file/d/1Cut_L9OOw3HJkxaj20xfKYt9hILa5xC9/view?usp=sharing]

#### Instructions: Download the file and place it in the root directory of this project before execution.

## Technical Stack
### Language: 
Python 3.14

### Libraries: 
OpenCV (cv2), Dlib, Pygame, Scipy

### Framework: 
HOG + Linear SVM for facial detection

## Installation & Setup
### Clone the Repository:


git clone https://github.com/[YOUR_USERNAME]/[YOUR_REPO_NAME].git
### Install Dependencies:


pip install opencv-python dlib pygame scipy
### Run the Application:


python drowsiness_detect.py
## Future Scope
Azure IoT Integration: Scaling the system for fleet management using Microsoft Azure for real-time safety analytics.

Edge Optimization: Using ONNX to deploy the model on mobile devices and dashcam hardware.

## License
This project is licensed under the MIT License.


[https://drive.google.com/file/d/1Cut_L9OOw3HJkxaj20xfKYt9hILa5xC9/view?usp=sharing]

# driver-drowsiness-detection-system
A real-time safety application built for the Microsoft Elevate Internship using Python 3.14 and OpenCV. It utilizes Haar Cascade classifiers to monitor driver fatigue and triggers an automated audio alarm within 0.5 seconds of detecting a microsleep event.

Microsoft Elevate AICTE Internship Project | Jan 20 - Feb 15, 2026

## Project Overview
This project is a real-time safety application designed to combat driver fatigue and prevent road accidents. Developed during a intensive 4-week internship, the system utilizes Computer Vision and Haar Cascade Classifiers to monitor driver alertness. It provides immediate audio-visual intervention when signs of drowsiness (microsleep) are detected.

## Key Features
### Real-Time Monitoring:
Captures live video at a stable 30 FPS to track facial state.

### Lightweight Architecture:
Optimized for modern environments (Python 3.13.5) using built-in OpenCV cascades, requiring no heavy external model files.

### Intelligent State Management: 
Triggers an automated alarm after 0.5 seconds (15 frames) of detected microsleep.

### Active-Stop Intervention: Features logic that immediately kills the alarm sound once the driver's eyes are detected open, ensuring minimal distraction after recovery.

## Technical Stack
### Language:
Python 3.13.5

### Core Libraries: *
### OpenCV (cv2): For image processing and object detection.

### Pygame:
For low-latency audio management and alarm state control.

### Model: 
Haar Cascade Classifiers (frontalface_default and haarcascade_eye).

## Installation & Setup
### 1. Clone the Repository:  
[https://github.com/kalpana-15-27/driver-drowsiness-detection-system.git]
### 2. Install Dependencies:
### opencv-python: 
Used for real-time video capture and implementing the Haar Cascade detection algorithms.

### pygame:
Utilized for its robust mixer module to handle the alert system's audio triggers and active-stop logic.
### 3. Run the Application:
Ensure your alarm.wav file is in the root directory, then run:

## Why Haar Cascades?
For this deployment, the project utilizes Haar Cascades instead of Dlib to ensure:

### Speed: 
Faster inference on standard laptop hardware and edge devices.

### Compatibility: 
Seamless integration with the latest Python versions without requiring heavy C++ build tools.

### Efficiency: 
Eliminates the need for 100MB+ external .dat files, making the repository standalone and portable.

## Future Scope
### Azure IoT Integration: 
Scaling the system for fleet management using Microsoft Azure for real-time safety analytics.

### Head Pose Estimation: 
Implementing 3D pose detection to differentiate between looking away (distraction) and closing eyes (drowsiness).
### Infrared (IR) Spectrum Integration: 
Transitioning from standard RGB to IR camera support to ensure 24/7 reliability, allowing the system to monitor facial landmarks even in zero-light driving conditions.

### Low-Light Robustness: 
Utilizing NIR (Near-Infrared) sensors to bypass the limitations of traditional Haar Cascades in nighttime environments.
## License
This project is licensed under the MIT License.

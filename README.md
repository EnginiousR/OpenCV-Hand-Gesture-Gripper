# 🖐️ Hand Gesture Controlled 3D-Printed Gripper  

## Overview  
This project demonstrates **real-time hand gesture recognition** using **OpenCV** and **MediaPipe**, integrated with an **Arduino-controlled 3D-printed robotic gripper**.  
By detecting an **open hand** or **closed fist** through a webcam, the system sends commands to the Arduino, which moves the gripper accordingly.  

The robotic arm’s structural parts were **3D-printed**, but the focus of this work is **the gripper mechanism and computer vision integration**.  

---

## Features  
- **Real-time gesture detection** with OpenCV + MediaPipe  
- **Seamless Arduino integration** via PySerial  
- **3D-printed gripper mechanism** for physical interaction  
- Simple, intuitive **open/close control** with natural hand gestures  
- Modular design — can be expanded for full robotic arm control  

---

## Technologies Used  
- **Python** (OpenCV, MediaPipe, PySerial)  
- **Arduino IDE** (Servo control)  
- **3D Printing** for gripper components  
- **USB Camera / Laptop Webcam**  

---

## Project Files  
| File | Description |
|------|-------------|
| `hand_control_gripper.py` | Python script for gesture detection & Arduino communication |
| `openCv_HandGripper.ino`  | Arduino code to control the gripper servo |

---

## How It Works  
1. **Webcam captures** the user’s hand in real-time.  
2. **MediaPipe Hand Tracking** detects 21 hand landmarks.  
3. The **gesture state** (open or closed) is calculated.  
4. **PySerial sends** a single character command (`O` for open, `G` for grab) to Arduino.  
5. Arduino **drives the servo** to open or close the 3D-printed gripper.  

---

## Setup & Usage  

### Arduino Setup  
- Connect your servo to Arduino:
  - **Signal** → Pin 9  
  - **VCC** → 5V  
  - **GND** → GND  
- Upload `openCv_HandGripper.ino` to your Arduino.  

### Python Environment  
conda create -n opencv-env python=3.10
conda activate opencv-env
pip install opencv-python mediapipe pyserial

### Python Environment
python hand_control_gripper.py


### Future Improvements
Add more gestures for advanced control (e.g., rotate wrist, partial grip).
Implement voice commands alongside gesture control.
Integrate feedback sensors in the gripper for pressure control.

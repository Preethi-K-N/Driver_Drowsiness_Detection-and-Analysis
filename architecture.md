# 🧠 Driver Drowsiness Detection System Architecture

## 🎯 Overview
A real-time, computer vision-based solution for detecting driver drowsiness. The system captures video frames, analyzes the driver's eye aspect ratio (EAR), and triggers alerts when fatigue is detected. All events and images are logged for review and accountability.

---

## 🏗️ Architecture Diagram


---

## ⚡️ Key Components
| Component       | Purpose                                                          |
|-----------------|------------------------------------------------------------------|
| **Camera Feed** | Captures live video frames from the driver's camera.            |
| **Face Mesh**   | Uses MediaPipe for extracting precise facial landmarks.           |
| **EAR Calculator** | Determines drowsiness by measuring eye aspect ratio across frames. |
| **Alert System**| Plays an alarm sound when drowsiness is detected.                |
| **Image Logger**| Captures and saves images when EAR threshold is exceeded.        |

---

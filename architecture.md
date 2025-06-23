# 🧠 Driver Drowsiness Detection System Architecture

## 🎯 Overview
A real-time, computer vision-based solution for detecting driver drowsiness. The system captures video frames, analyzes the driver's eye aspect ratio (EAR), and triggers alerts when fatigue is detected. All events and images are logged for review and accountability.

---

## 🏗️ Architecture Diagram

                        +------------------+
                        |     Webcam       |
                        +--------+---------+
                                 |
                                 v
                      +----------------------+
                      |  MediaPipe Face Mesh |
                      | (Eye landmark detect)|
                      +----------------------+
                                 |
                                 v
                      +----------------------+
                      | EAR Calculation      |
                      | (Eye Aspect Ratio)   |
                      +----------------------+
                                 |
                      EAR < Threshold for N frames
                                 |
                                 v
                      +---------------------+           +-----------------+
                      | Alert Trigger       |----->     |  Save Images    |
                      | (Alarm Sound, Logs) |           +-----------------+
                      +---------------------+          
                                 |
                                 v
                      +---------------------+          +-----------------+
                      |  Analysis Scripts   | ----->   |  Trends & Plots |
                      +---------------------+          +-----------------+



---

## ⚡️ Key Components
| Component          | Purpose                                                            |
|--------------------|--------------------------------------------------------------------|
| **Camera Feed**    | Captures live video frames from the driver's camera.               |
| **Face Mesh**      | Uses MediaPipe for extracting precise facial landmarks.            |
| **EAR Calculator** | Determines drowsiness by measuring eye aspect ratio across frames. |
| **Alert System**   | Plays an alarm sound when drowsiness is detected.                  |
| **Image Logger**   | Captures and saves images when EAR threshold is exceeded.          |


---

## ✅ Benefits
- Enables **early detection** of fatigue and alerts the driver.  
- Provides **logs and images** for post-analysis and review.  
- Supports **scalability** for deployments in transport, logistics, and public services.  
- Enables seamless **integration** with dashboards or mobile alerts.


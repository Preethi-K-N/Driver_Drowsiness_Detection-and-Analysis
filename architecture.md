# 🧠 **Driver Drowsiness Detection System Architecture**

## 🎯 _**Overview**_
A real-time, computer vision-based system that detects drowsiness by analyzing eye and mouth movements using **EAR (Eye Aspect Ratio)** and **MAR (Mouth Aspect Ratio)**. Upon detection, it triggers an audible alert and logs image clippings. The analysis module visualizes trends of drowsiness incidents across time.

---

## 🏗️ _**Architecture Diagram**_
                    +------------------+
                    |     Webcam       |
                    +--------+---------+
                             |
                             v
              +------------------------------+
              | Face Alignment (68 landmarks)|
              +------------------------------+
                             |
             +--------------+---------------+
             |                              |
             v                              v
   +------------------+            +------------------+
   | EAR Calculation  |            | MAR Calculation  |
   +------------------+            +------------------+
             |                              |
 EAR < 0.30 for N frames         MAR > 0.65 for N frames
             |                              |
             +--------------+---------------+
                            |
                            v
            +-----------------------------+
            |  Alert System               |
            | (Alarm + Image Clipping x3) |
            +-----------------------------+
                            |
                            v
            +------------------------------+
            | Analysis Module (analyze.py) |
            +------------------------------+
                            |
                            v
            +-----------------------------+
            | Daily/Hourly Trend Plots    |
            +-----------------------------+


---

## ⚡️ _**Key Components**_

| **Component**        | **Purpose**                                                                  |
|----------------------|------------------------------------------------------------------------------|
| **Webcam Feed**      | Captures real-time video input of the driver's face.                         |
| **Face Alignment**   | Detects 68 facial landmarks using `face_alignment` library.                  |
| **EAR Calculator**   | Calculates Eye Aspect Ratio to detect blinking and closed eyes.              |
| **MAR Calculator**   | Calculates Mouth Aspect Ratio to detect yawning.                             |
| **Alert System**     | Triggers alarm (via `pygame`) and saves 3 images when drowsiness is detected.|
| **Image Logger**     | Stores images in timestamped folders under `image_clippings/`.               |
| **Analysis Module**  | Analyzes logs using `pandas` and visualizes trends using `matplotlib`.       |

---

## ✅ _**Benefits**_

- Detects both **eye closure** and **yawning** to improve accuracy.
- Automatically **saves evidence images** on detection.
- Plots **daily and hourly trends** for post-event review.
- Works offline in **real-time** with fast execution.
- Adaptable for **fleet monitoring, transport safety**, and smart vehicle systems.

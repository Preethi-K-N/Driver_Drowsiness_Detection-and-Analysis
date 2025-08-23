# 💤 Driver Drowsiness Detection System

<img width="2648" height="1536" alt="Gemini_Generated_Image_ng0zv6ng0zv6ng0z" src="https://github.com/user-attachments/assets/168cd2e6-b49f-4b0f-bbd7-ff7e38893a00" />


A real-time computer vision project that monitors eye and mouth movement using a webcam feed, providing alerts when signs of drowsiness are detected. It also captures image evidence and visualizes drowsiness patterns over time.

🚗 **Use Case**: Designed for drivers, long-distance riders, and commercial vehicle operators where fatigue could lead to accidents.

🧠 **Technologies**: 
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue.svg)
![Face Alignment](https://img.shields.io/badge/Face_Alignment-1.x-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-purple.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.x-yellow.svg)
![SciPy](https://img.shields.io/badge/SciPy-1.x-brightgreen.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.x-red.svg)

---

## 🦄 _**Code Requirements**_
- Python 3.9 or later
- A working virtual environment (`venv`) for isolation
- Required libraries: `opencv-python`, `numpy`, `pygame`, `scipy`, `face-alignment`, `pandas`, `matplotlib`

---

## 🔍 _**Problem Statement**_

Fatigue while driving is one of the major causes of road accidents. Human monitoring isn't reliable for long hours of travel. This system provides a real-time alert mechanism when drowsiness is detected using Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) calculations, helping prevent accidents proactively.

---

## 🎯 _**Key Features**_

- 🔄 Real-time webcam-based monitoring
- 👁 EAR and 👄 MAR-based fatigue detection
- 🚨 Audio alarm when drowsiness is detected
- 🖼️ Saves 3 image clippings per alert
- 📊 Analyzes and plots drowsiness trends by day and hour
- ✅ Clean and beginner-friendly Python interface

---

## 🛠️ _**Tech Stack**_
- **Python 3.x** - Programming Language
- **OpenCV** - Image processing and webcam capture
- **face_alignment** - 2D facial landmarks extraction
- **SciPy** - EAR and MAR calculation
- **Pygame** - Alarm playback
- **Pandas** - Logging and analysis
- **Matplotlib** - Data visualization

---

## 📌 _**How It Works**_
- `face_alignment` detects 68 facial landmarks
- EAR (Eye Aspect Ratio) is calculated from eye landmarks
- MAR (Mouth Aspect Ratio) is calculated from mouth landmarks
- If EAR < 0.30 or MAR > 0.65 for 10 consecutive frames → Drowsiness Detected
- Alarm plays, and 3 real-time images are saved in a folder (with timestamps)
- Later, `analyze.py` is used to visualize the daily and hourly drowsiness trends

---

## 👨‍🔬 _**Algorithm Overview**_
This system uses facial landmarks to monitor drowsiness based on eye and mouth movements.

### 👁️ _**Eye and 👄 Mouth Landmark Mapping**_

<img width="685" height="230" alt="ddd2" src="https://github.com/user-attachments/assets/d4b176e8-2878-4e50-9928-5087b5fcf876" />


### 👁️ _Eye Aspect Ratio (EAR)_
Detects eye closure using 6 key landmarks around each eye.

**Formula:**
```
EAR = (‖p2 - p6‖ + ‖p3 - p5‖) / (2 × ‖p1 - p4‖)
```
EAR drops when eyes close.

**Threshold:**
- If EAR < 0.30 for several consecutive frames → **Drowsiness Detected**

### 👄 _Mouth Aspect Ratio (MAR)_
Detects yawning using 8–10 mouth landmarks.

**Formula:**
```
MAR = ‖p63 - p67‖ / ‖p61 - p65‖
```
MAR increases when mouth opens wide.

**Threshold:**
- If MAR > 0.65 → **Yawning Detected**

### 🔔 _Alert Trigger_
When EAR < 0.30 or MAR > 0.65 for 10+ consecutive frames:

- 📢 Alarm is played
- 📸 3 images are saved
- ⚠️ Drowsiness warning displayed on screen

---

## 🐉 _**Execution Steps**_

1. **Run Detection (Real-Time Alert + Image Capture)**
```bash
python detector.py
```
2. **Run Analysis (Trends Visualization)**
```bash
python analyze.py
```
> Make sure all images are stored in the `image_clippings` folder as expected.

---

## 🗂 _**Folder Structure**_
```
Driver Drowsiness Detection
│
├── detector.py             # Real-time detection
├── analyze.py              # Analysis and plotting
├── alarm.wav               # Alarm sound file
├── image_clippings/        # Automatically created folders with saved alert images
├── drowsiness_trends/      # Folder for saving plots
├── README.md               # This file
└── ...
```

---

## 📌 _**Citation**_
```bibtex
@article{Driver_Drowsiness_Detection_and_Analysis,
  author  = {Preethi K.N},
  journal = {https://github.com/preethikn/Driver_Drowsiness_Detection-and-Analysis},
  month   = {07},
  title   = {Driver Drowsiness Detection using EAR, MAR and Analysis},
  year    = {2025}
}
```

---

## 📚 _**References**_
- [Face Alignment Library](https://github.com/1adrianb/face-alignment)
- [EAR method: Soukupová & Čech - Real-Time Eye Blink Detection](https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)
- [PyImageSearch: Facial Landmarks & Drowsiness Detection](https://pyimagesearch.com/)

💤 Driver Drowsiness Detection System

A real-time computer vision project that monitors eye movement using webcam feed and alerts users when signs of drowsiness are detected.

> 🚗 **Use Case**: Designed for drivers, long-distance riders, and commercial vehicle operators where fatigue could lead to accidents.  
> 🧠 **Technologies**: OpenCV, MediaPipe, Pandas, Matplotlib, NumPy, SciPy

---

🦄 Code Requirements 
The example code is implemented in Python 3.9 or higher and may not be compatible with older versions.
Please ensure you have the following:
•	Python 3.9 or later
•	A working virtual environment (venv) for isolation

---

 🔍 Problem Statement

Fatigue while driving is one of the major causes of road accidents. Human monitoring isn't reliable, especially for long hours of travel. This system provides a real-time alert mechanism when drowsiness is detected using the **Eye Aspect Ratio (EAR)** method and helps prevent accidents proactively.

---

 🎯 Key Features

- 🔄 **Real-time webcam-based monitoring**
- 🚨 **Audio alert** when drowsiness is detected
- 🖼️ **Saves image clippings** upon detection
- 📊 **Analyzes drowsiness patterns** with visual trends
- 📅 **Supports daily/hourly/weekly analysis**
- ✅ Easy-to-use Python interface

---

 🛠️ Tech Stack
 
- Python 3.x	 - Programming Language
- OpenCV    	 - Image processing and webcam capture
- MediaPipe	  - Face and eye landmark detection
- SciPy       - Eye Aspect Ratio calculation
- Pandas	     - Logging and trend analytics
- Matplotlib	 - Plotting and visualization
- SimpleAudio - 	Alarm playback

---

 📌 How It Works

- Media Pipe detects facial landmarks
- EAR (Eye Aspect Ratio) is calculated from eye landmarks
- If EAR < 0.25 for 48 consecutive frames, it is considered drowsiness
- A warning message is shown, an alarm sounds, and 3 images are saved
- Data is logged for later analysis

---

👨‍🔬 Algorithm 

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye.
It checks 20 consecutive frames and if the Eye Aspect ratio is less than 0.30, Alert is generated.

---

 👁 Eye Aspect Ratio Formula

 
![image](https://github.com/user-attachments/assets/21b619a9-56e9-47f6-bc3b-f5003fd84880)
![image](https://github.com/user-attachments/assets/fcee91f5-efc8-4d08-b6c8-ec621e74b518)
![image](https://github.com/user-attachments/assets/0cc55a1a-4f92-40e4-8e3e-1a3bd5e05845)

---

🐉 Execution
To run the code, make sure you have activated the virtual environment and installed the required dependencies. Then run the following command:


```bash
python Drowsiness_Detection.py
```


📌 Cite Us

To cite this project, use the following format:

```bibtex
@article{Driver_Drowsiness_Detection_and_Analysis,
  author  = {Preethi K.N},
  journal = {https://github.com/preethikn/driver-drowsiness-detection},
  month   = {06},
  title   = {Driver Drowsiness Detection using EAR and Analysis},
  year    = {2025}
}
```

## 📚 References

- [MediaPipe by Google](https://google.github.io/mediapipe/)
- [PyImageSearch Blog by Adrian Rosebrock](https://pyimagesearch.com)
- EAR methodology inspired by Tereza Soukupova and Jan Cech’s work on eye blink detection

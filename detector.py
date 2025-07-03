# === detector.py ===
import cv2
import numpy as np
import os
import datetime
from scipy.spatial import distance as dist
import pygame
import face_alignment

# ==== CONFIGURATION ====
EAR_THRESHOLD = 0.30
MAR_THRESHOLD = 0.65
CONSEC_FRAMES = 10
NUM_IMAGES = 3
IMAGE_FOLDER = r"D:\Preethi\OneDrive\Desktop\GIT Files\Driver Drowsiness Detection\image_clippings"
ALARM_FILE = "alarm.wav"

# ==== PREPARE ====
os.makedirs(IMAGE_FOLDER, exist_ok=True)
pygame.mixer.init()
if not pygame.mixer.get_init():
    print("⚠️ Pygame mixer failed to initialize!")
pygame.mixer.music.load(ALARM_FILE)

fa = face_alignment.FaceAlignment('2D', flip_input=False, device='cpu')

LEFT_EYE = [36, 37, 38, 39, 40, 41]
RIGHT_EYE = [42, 43, 44, 45, 46, 47]
MOUTH = [60, 64, 62, 66, 63, 65, 61, 67, 59, 55]

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def mouth_aspect_ratio(mouth):
    A = dist.euclidean(mouth[2], mouth[3])
    B = dist.euclidean(mouth[0], mouth[1])
    return A / B

cap = cv2.VideoCapture(0)
counter = 0
alarm_on = False

print("✅ Drowsiness detection started... Press 'q' or 'Esc' to quit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        landmarks = fa.get_landmarks_from_image(rgb)

        if landmarks is None:
            print("😕 No face detected.")
            continue

        shape = landmarks[0]
        left_eye = np.array([shape[i] for i in LEFT_EYE])
        right_eye = np.array([shape[i] for i in RIGHT_EYE])
        mouth = np.array([shape[i] for i in MOUTH])

        ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
        mar = mouth_aspect_ratio(mouth)

        if ear < EAR_THRESHOLD or mar > MAR_THRESHOLD:
            counter += 1
            if counter >= CONSEC_FRAMES:
                if not alarm_on:
                    alarm_on = True
                    pygame.mixer.music.play(-1)
                    print("🔔 Alarm should be playing now.")

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                folder = datetime.datetime.now().strftime("%Y-%m-%d")
                path = os.path.join(IMAGE_FOLDER, folder)
                os.makedirs(path, exist_ok=True)

                for i in range(NUM_IMAGES):
                    filename = f"{timestamp}_{i+1}.jpg"
                    cv2.imwrite(os.path.join(path, filename), frame)
                    cv2.putText(frame, f"DROWSINESS ALERT! Saved {i+1}/{NUM_IMAGES}",
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.imshow("Driver Drowsiness Detection", frame)
                    cv2.waitKey(200)
                counter = 0
        else:
            counter = 0
            if alarm_on:
                pygame.mixer.music.stop()
                alarm_on = False

        cv2.putText(frame, "Press 'Q' or 'Esc' to quit", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow("Driver Drowsiness Detection", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            print("❌ Stopped.")
            break

except Exception as e:
    print("⚠️ Error:", e)

finally:
    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.quit()

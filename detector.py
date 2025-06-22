import cv2
import mediapipe as mp
import numpy as np
import os
import datetime
from scipy.spatial import distance as dist
import simpleaudio as sa

# ==== CONFIGURATION ====
EAR_THRESHOLD = 0.30
CONSEC_FRAMES = 48
IMAGE_FOLDER = "image_clippings"
ALARM_FILE = "alarm.wav"
NUM_IMAGES = 3  # Capture this many images per alert

# ==== PREPARE ====
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Load alarm sound
wave_obj = sa.WaveObject.from_wave_file(ALARM_FILE)

# Prepare face mesh detector
mp_face_mesh = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5
)

# Capture
cap = cv2.VideoCapture(0)
counter = 0
print("✅ Starting drowsiness detection...")

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = mp_face_mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            h, w = frame.shape[:2]

            left_eye_idx = [362, 385, 387, 263, 373, 380]
            right_eye_idx = [33, 160, 158, 133, 153, 144]

            left_eye = np.array([[int(landmarks[i].x*w), int(landmarks[i].y*h)] for i in left_eye_idx])
            right_eye = np.array([[int(landmarks[i].x*w), int(landmarks[i].y*h)] for i in right_eye_idx])
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0

            if ear < EAR_THRESHOLD:
                counter += 1
                if counter >= CONSEC_FRAMES:
                    # Trigger alert
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    date_folder = datetime.datetime.now().strftime("%Y-%m-%d")
                    date_folder_path = os.path.join(IMAGE_FOLDER, date_folder)
                    os.makedirs(date_folder_path, exist_ok=True)

                    for i in range(NUM_IMAGES):
                        img_name = f"{timestamp}_{i+1}.jpg"
                        img_path = os.path.join(date_folder_path, img_name)
                        cv2.imwrite(img_path, frame)
                        wave_obj.play()
                        cv2.putText(
                            frame, f"DROWSINESS ALERT! Saved {i+1}/{NUM_IMAGES}",
                            (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
                        )
                        cv2.imshow('Driver Drowsiness Detection', frame)
                        cv2.waitKey(200)  # brief wait between captures

                    counter = 0  # reset counter after capturing images
            else:
                counter = 0

        cv2.imshow('Driver Drowsiness Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("❌ Quitting...")
            break
except Exception as e:
    print("Error:", e)
finally:
    cap.release()
    cv2.destroyAllWindows()

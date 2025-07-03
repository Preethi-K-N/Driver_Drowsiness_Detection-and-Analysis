import os
import re
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Configuration
IMAGE_FOLDER = r"D:\Preethi\OneDrive\Desktop\GIT Files\Driver Drowsiness Detection\image_clippings"
OUTPUT_DIR = "drowsiness_trends"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ Gather image files
image_files = []
for root, dirs, files in os.walk(IMAGE_FOLDER):
    for f in files:
        if f.endswith(".jpg"):
            image_files.append(os.path.join(root, f))

# ✅ Parse timestamps
timestamps = []
for path in image_files:
    name = os.path.basename(path)
    match = re.search(r'(\d{8}_\d{6})', name)
    if match:
        timestamps.append(pd.to_datetime(match.group(1), format="%Y%m%d_%H%M%S"))
    else:
        print(f"⚠️ Could not parse timestamp: {name}")

df = pd.DataFrame({"Timestamp": timestamps})
df.sort_values("Timestamp", inplace=True)

# 📊 Plot 1: Alerts per Day
df["date"] = df["Timestamp"].dt.date
daily = df.groupby("date").size()
plt.figure(figsize=(10, 5))
daily.plot(marker='o')
plt.title("Drowsiness Alerts per Day")
plt.xlabel("Date")
plt.ylabel("Images Captured")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "daily_alerts.png"))
plt.close()

# 📊 Plot 2: Alerts per Hour
df["hour"] = df["Timestamp"].dt.hour
hourly = df.groupby("hour").size()
plt.figure(figsize=(8, 5))
hourly.plot(kind='bar', color='orange')
plt.title("Drowsiness Alerts per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Images Captured")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "hourly_alerts.png"))
plt.close()

print(f"✅ Total images: {len(df)}")
print(f"📁 Plots saved in: {os.path.abspath(OUTPUT_DIR)}")

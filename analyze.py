import os
import re
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Configuration
IMAGE_FOLDER = "image_clippings"
OUTPUT_DIR = "drowsiness_trends"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ Gather all image files
image_files = []
for root, dirs, files in os.walk(IMAGE_FOLDER):
    for f in files:
        if f.endswith(".jpg"):
            image_files.append(os.path.join(root, f))

# ✅ Parse timestamps from file names
timestamps = []
for path in image_files:
    name = os.path.basename(path)
    match = re.search(r'(\d{8}_\d{6})', name)  # matches e.g. 20250620_223555
    if match:
        timestamps.append(pd.to_datetime(match.group(1), format="%Y%m%d_%H%M%S"))
    else:
        print(f"⚠️ Could not parse timestamp in {path}")

df = pd.DataFrame({"Timestamp": timestamps})
df.sort_values('Timestamp', inplace=True)

print(f"✅ Total drowsiness images detected: {len(df)}")

# 📊 Plot 1: Images per day
df['date'] = df['Timestamp'].dt.date
daily_counts = df.groupby('date').size()
plt.figure(figsize=(10, 5))
daily_counts.plot(marker='o')
plt.title('Drowsiness Alerts per Day')
plt.xlabel('Date')
plt.ylabel('Number of Images Captured')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'daily_alerts.png'))
plt.close()

# 📊 Plot 2: Images per Hour
df['hour'] = df['Timestamp'].dt.hour
hourly_counts = df.groupby('hour').size()
plt.figure(figsize=(8, 5))
hourly_counts.plot(kind='bar', color='orange')
plt.title('Drowsiness Alerts per Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Images Captured')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'hourly_alerts.png'))
plt.close()

# ✅ Summary
print(f"✅ Analysis complete — Plots saved in '{OUTPUT_DIR}'")


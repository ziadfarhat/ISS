import cv2
import numpy as np
from PIL import Image
import numpy as np

# Load the video file
video_path = 'iss.mp4'  # Video Path
cap = cv2.VideoCapture(video_path)

# Collect frames from the video
frames = []
frame_count = 0

# Capture every 5th frame for a sample overview
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % 5 == 0:
        frames.append(frame)
    frame_count += 1

cap.release()

# Function to enhance shadow details in frames
def enhance_frame_contrast(frame):
    # Convert to grayscale for better shadow visualization
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization to improve contrast
    enhanced = cv2.equalizeHist(gray)
    # Convert back to a colored frame with enhanced contrast
    enhanced_colored = cv2.merge([enhanced, enhanced, enhanced])
    return enhanced_colored

# Apply enhancement to each sampled frame
enhanced_frames = [enhance_frame_contrast(frame) for frame in frames[:3]]

# Display the enhanced frames
for i, enhanced_frame in enumerate(enhanced_frames):
    img = Image.fromarray(enhanced_frame)
    img.save(f"enhanced_frame_{i}.jpg")  # Saves each enhanced frame as a separate image file

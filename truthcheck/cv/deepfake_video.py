import cv2
from deepface import DeepFace

def analyze_video(video_file):
    temp_path = f"temp_{video_file.name}"
    with open(temp_path, "wb") as f:
        f.write(video_file.read())

    cap = cv2.VideoCapture(temp_path)
    frame_count = 0
    fake_count = 0

    while True:
        ret, frame = cap.read()
        if not ret or frame_count > 10:  # Analyze first 10 frames
            break
        try:
            DeepFace.analyze(frame, actions=['emotion'], enforce_detection=True)
        except:
            fake_count += 1
        frame_count += 1

    if fake_count > 3:
        return "❌ Likely Deepfake Video"
    else:
        return "✅ Likely Real Video"

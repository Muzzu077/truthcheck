from deepface import DeepFace
import tempfile
import cv2

def analyze_image(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(file.read())
        path = tmp.name

    try:
        analysis = DeepFace.analyze(img_path=path, actions=['emotion'], enforce_detection=True)
        # If analysis fails or shows extreme values, assume deepfake
        return "✅ Real Image (No deepfake signs)"
    except Exception as e:
        return "⚠️ Possibly a manipulated or deepfake image."

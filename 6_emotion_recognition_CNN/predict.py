import sys
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = "emotion_model.h5"
IMG_SIZE = 48
CLASS_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

def predict(image_path):
    if not os.path.exists(image_path):
        print(f"[ERROR] Image path does not exist: {image_path}")
        return

    if not os.path.exists(MODEL_PATH):
        print(f"[ERROR] Trained model file '{MODEL_PATH}' not found! Run train.py first.")
        return

    print("[INFO] Loading model...")
    model = load_model(MODEL_PATH)

    img = cv2.imread(image_path)
    if img is None:
        print(f"[ERROR] Could not read image at: {image_path}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        print("[WARNING] No face detected by OpenCV. Resizing the full image.")
        cropped_face = gray
    else:
        x, y, w, h = faces[0]
        cropped_face = gray[y:y+h, x:x+w]

    resized = cv2.resize(cropped_face, (IMG_SIZE, IMG_SIZE))
    normalized = resized.astype("float32") / 255.0
    input_tensor = np.expand_dims(normalized, axis=(0, -1))

    probabilities = model.predict(input_tensor)[0]
    predicted_idx = np.argmax(probabilities)
    predicted_emotion = CLASS_LABELS[predicted_idx]
    confidence = probabilities[predicted_idx] * 100

    print("\n" + "=" * 38)
    print(f" Analyzed File: {image_path}")
    print(f" Prediction:    {predicted_emotion}")
    print(f" Confidence:    {confidence:.2f}%")
    print("=" * 38)
    print(" Class Probabilities:")
    for label, prob in zip(CLASS_LABELS, probabilities):
        print(f"   {label:<10}: {prob * 100:.2f}%")
    print("=" * 38 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <path_to_image>")
    else:
        predict(sys.argv[1])
# 🎭 Facial Emotion Recognition (CNN)

This project builds an end-to-end **Facial Emotion Recognition System** using a Deep Convolutional Neural Network (CNN) in TensorFlow/Keras. The model processes 48x48 grayscale facial images and classifies human expressions into 7 distinct emotion categories: **Angry, Disgust, Fear, Happy, Neutral, Sad, and Surprise**.

Included in this directory is also a standalone inference CLI tool (`predict.py`) that uses OpenCV Haar Cascade face detection to locate faces in any image, preprocess them, and output real-time emotion probability distributions.

---

## 📊 Dataset

The model is trained on the popular **FER-2013 (Facial Expression Recognition)** dataset.

* **Kaggle Link:** [FER-2013 Dataset on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)
* **Image Specs:** 48x48 resolution, Single-channel Grayscale.
* **Target Classes (7):**
  1. `angry`
  2. `disgust`
  3. `fear`
  4. `happy`
  5. `neutral`
  6. `sad`
  7. `surprise`
* **Directory Structure:**
  ```text
  Dataset/
  ├── train/
  │   ├── angry/
  │   ├── disgust/
  │   ├── fear/
  │   ├── happy/
  │   ├── neutral/
  │   ├── sad/
  │   └── surprise/
  └── test/
      ├── angry/
      └── ...
  ```

---

## 🏗️ CNN Model Architecture

The architecture consists of 3 stacked VGG-style Convolutional blocks with batch normalization, max pooling, and spatial dropout, followed by a dense classification head.

```text
Input (48x48x1 Grayscale)
    │
    ├── Conv Block 1: [Conv2D(64) → BatchNorm → Conv2D(64) → BatchNorm → MaxPool(2x2) → Dropout(0.25)]
    ├── Conv Block 2: [Conv2D(128) → BatchNorm → Conv2D(128) → BatchNorm → MaxPool(2x2) → Dropout(0.25)]
    ├── Conv Block 3: [Conv2D(256) → BatchNorm → Conv2D(256) → BatchNorm → MaxPool(2x2) → Dropout(0.25)]
    │
    ├── Flatten
    ├── Dense(256) → BatchNorm → Dropout(0.50)
    └── Output: Dense(7, Softmax)
```

---

## 🛠️ Data Preprocessing & Augmentation

To handle variation in head poses and prevent overfitting, real-time image augmentation is applied via `ImageDataGenerator`:
* **Rescaling:** Pixel intensities normalized to `[0.0, 1.0]`.
* **Rotation Range:** $\pm 15^\circ$ random rotations.
* **Shifts:** $\pm 10\%$ horizontal and vertical translation.
* **Shearing & Zooming:** $0.1$ intensity scale.
* **Flips:** Horizontal flipping enabled for pose symmetry.

---

## ⚙️ Training & Optimization Callbacks

* **Optimizer:** Adam (Initial `learning_rate = 0.001`).
* **Loss Function:** `categorical_crossentropy`.
* **Callbacks Implemented:**
  * **`ModelCheckpoint`:** Automatically saves the best model weights to `emotion_model.h5` based on validation accuracy (`val_accuracy`).
  * **`EarlyStopping`:** Stops training if validation loss does not improve for 7 consecutive epochs (`patience=7`).
  * **`ReduceLROnPlateau`:** Dynamically drops the learning rate by a factor of $0.2$ if validation loss plateaus for 3 epochs.

---

## 🔍 Inference & Face Detection (`predict.py`)

A custom Python script (`predict.py`) allows testing on raw images:
1. Uses OpenCV's **Haar Cascade (`haarcascade_frontalface_default.xml`)** to detect faces in input images.
2. Crops and resizes the primary detected face to `48x48` grayscale.
3. Passes the preprocessed face tensor into `emotion_model.h5`.
4. Prints prediction summary and confidence scores across all 7 emotion classes.

### Command Usage:
```bash
python predict.py img1.jpg
```

### Sample Output:
```text
======================================
 Analyzed File: img1.jpg
 Prediction:    Happy
 Confidence:    96.42%
======================================
 Class Probabilities:
   Angry     : 0.12%
   Disgust   : 0.01%
   Fear      : 0.45%
   Happy     : 96.42%
   Neutral   : 2.10%
   Sad       : 0.80%
   Surprise  : 0.10%
======================================
```

---

## 🚀 How to Run

1. **Install Dependencies:**
   ```bash
   pip install tensorflow opencv-python numpy matplotlib
   ```

2. **Download Dataset:**
   Download FER-2013 from Kaggle and extract into the `Dataset/` folder (`Dataset/train` and `Dataset/test`).

3. **Train the Model:**
   Launch and execute `emotion_recogniser.ipynb` using Jupyter:
   ```bash
   jupyter notebook emotion_recogniser.ipynb
   ```

4. **Predict Emotion on New Images:**
   ```bash
   python predict.py <path_to_image>
   ```

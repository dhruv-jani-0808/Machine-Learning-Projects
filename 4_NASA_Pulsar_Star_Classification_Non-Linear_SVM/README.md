# 🌌 NASA Pulsar Star Classification (Non-Linear SVM)

This project classifies deep-space radio signals recorded by the **HTRU2 survey** as either background Cosmic Noise (0) or genuine Pulsar Stars (1). Pulsars are rare, rapidly rotating neutron stars that emit highly periodic electromagnetic pulses — identifying them reliably amidst massive amounts of radio noise is a classic imbalanced binary classification challenge.

---

## 📊 Dataset

The dataset is derived from the **High Time Resolution Universe Survey (HTRU2)**, publicly available on the UCI Machine Learning Repository.

* **Kaggle Link:** [Pulsar Star Dataset — HTRU2](https://www.kaggle.com/datasets/colearninglounge/predicting-pulsar-starhtru2)
* **Scale:** **17,898 samples** with **8 numerical features** and **1 binary target column**.
* **Class Imbalance:** Only ~9.1% of samples are genuine Pulsar Stars, making this a highly imbalanced dataset.
* **Dependent Variable (Target):** `target` — `1` for a real Pulsar Star, `0` for Radio Frequency Interference / Cosmic Noise.

---

## 🛠️ Feature Engineering & Preprocessing

Each signal is represented by 8 statistical features extracted from two key waveform measurements:

### 1. Integrated Pulse Profile Statistics
* `mean_profile` — Mean of the integrated profile.
* `std_profile` — Standard deviation of the integrated profile.
* `kurtosis_profile` — Excess kurtosis of the integrated profile.
* `skewness_profile` — Skewness of the integrated profile.

### 2. DM-SNR (Dispersion Measure Signal-to-Noise Ratio) Curve Statistics
* `mean_dmsnr` — Mean of the DM-SNR curve.
* `std_dmsnr` — Standard deviation of the DM-SNR curve.
* `kurtosis_dmsnr` — Excess kurtosis of the DM-SNR curve.
* `skewness_dmsnr` — Skewness of the DM-SNR curve.

**Feature Scaling:** All 8 features are standardized using `StandardScaler` (zero mean, unit variance), which is critical for SVM performance since the kernel distance calculations are sensitive to feature magnitude differences.

---

## 🤖 Model & Training

* **Algorithm:** Supervised Binary Classification using a **Support Vector Machine (SVM)** with an **RBF (Radial Basis Function / Gaussian) Kernel** (`sklearn.svm.SVC`).
* **Why RBF?** The 8 features are not linearly separable. The RBF kernel implicitly maps the data into an infinite-dimensional feature space, allowing the SVM to find a non-linear decision boundary (hyperplane) that cleanly separates pulsars from noise.
* **Train/Test Split:** 80/20 stratified split to preserve the original class distribution in both sets.
* **Visualization:** PCA is used to compress the 8D feature space to 2 principal components, allowing the non-linear decision boundary to be visualized on a 2D scatter plot.

---

## ⚙️ Hyperparameter Tuning (GridSearchCV)

To improve performance on the imbalanced pulsar class, `GridSearchCV` is used with 5-fold cross-validation optimizing for **F1-Score**:

| Hyperparameter | Values Searched |
| :--- | :--- |
| `C` (Regularization) | `[0.1, 1, 10, 100]` |
| `gamma` (Kernel Width) | `['scale', 'auto', 0.01, 0.1]` |
| `class_weight` | `[None, 'balanced']` |

---

## 📈 Results & Performance

| Metric | Default SVM | Tuned SVM |
| :--- | :--- | :--- |
| Accuracy | ~97.8% | ~98.2% |
| ROC AUC | ~0.9960 | ~0.9975 |
| Pulsar Recall | ~88% | ~93%+ |

The tuned model significantly improves Pulsar Star recall, which is the critical metric — missing a real pulsar (False Negative) is more costly than a false alarm (False Positive) in an astronomical discovery context.

---

## ⚙️ How to Run

1. Make sure you have the required libraries installed:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```
2. Download the dataset from the [Kaggle Dataset Page](https://www.kaggle.com/datasets/colearninglounge/predicting-pulsar-starhtru2) and place `HTRU_2.csv` in the `Dataset/` directory.
3. Launch and run the Jupyter notebook:
   ```bash
   jupyter notebook Star_classification.ipynb
   ```

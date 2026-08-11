---
title: Smart Image Compressor K Means
emoji: 🖼️
colorFrom: blue
colorTo: cyan
sdk: docker
app_port: 7860
short_description: Unsupervised K-Means image compression & color quantization app.
---

# 🖼️ Smart Image Compressor via K-Means Clustering

An end-to-end Unsupervised Machine Learning web application and portfolio project that compresses images using **K-Means Clustering** color quantization. The system intelligently reduces an image's unique color palette into $K$ cluster centroids, adaptively fitting photos under user-defined target file sizes (e.g. Max 100 KB).

---

## 🧠 Core Machine Learning Concept

### Unsupervised Color Quantization
In digital images, each pixel is a point in a 3D RGB color space:
$$\text{Pixel} = (R, G, B) \quad \text{where } R, G, B \in [0, 255]$$

A high-resolution image often contains millions of unique colors. **K-Means Clustering** treats all pixel colors as 3D data points and groups them into $K$ clusters:
1. **$k$-means++ Initialization**: Intelligently selects initial centroids spaced far apart in RGB space to ensure fast convergence.
2. **Cluster Centroid Optimization**: Minimizes the Within-Cluster Sum of Squares (Inertia / SSE):
   $$J = \sum_{i=1}^{K} \sum_{x \in S_i} \|x - \mu_i\|^2$$
3. **Quantization**: Every original pixel is replaced by the RGB values of its assigned cluster centroid $\mu_i$, significantly reducing entropy and file byte size.

### Adaptive Target Size Search Algorithm
Instead of forcing users to guess the optimal number of clusters, the backend executes an **adaptive optimization loop**:
- Measures original image file size in memory.
- Evaluates decreasing cluster values $K \in [32, 16, 8, 4, 2]$ and image dimension scaling.
- Guarantees the compressed image meets the user's target file size (e.g. $\le 100\text{ KB}$) with optimal visual fidelity.

---

## 💻 Tech Stack & Architecture

- **Backend Engine**: Python, `FastAPI`, `scikit-learn` (`sklearn.cluster.KMeans`), `NumPy`, `Pillow` (PIL).
- **Frontend Dashboard**: HTML5, Vanilla CSS3 (Glassmorphism design system & full-width responsive grid), JavaScript (DOM manipulation & AJAX).
- **Containerization**: `Dockerfile` & `docker-compose.yml` for isolated container deployment.
- **Playground**: `model_experimentation.ipynb` Jupyter Notebook for mathematical visual exploration (3D RGB scatter plots & Elbow Curve).

---

## ✨ Features & Interactive Web Dashboard

- **Full-Color Target KB Compression**: Automatically quantizes colors and optimizes scale to fit under any max KB limit.
- **Grayscale Quantization**: Converts colorful photos to grayscale and quantizes intensity values into distinct gray shades.
- **Quick Presets**: Single-click target size buttons (`50 KB`, `100 KB`, `250 KB`, `500 KB`).
- **Interactive Split Slider**: Real-time Before/After image comparison slider to inspect visual quality side-by-side.
- **Extracted Centroid Swatches**: Displays the $K$ RGB/Hex colors chosen by the model with click-to-copy functionality.
- **Download Output**: Direct export of compressed images.

---

## ⚙️ How to Run

### Option 1: Local FastAPI Server
1. Activate your Conda/Python environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the FastAPI server using Uvicorn:
   ```bash
   uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```
3. Open your browser and navigate to `http://127.0.0.1:8000`.

### Option 2: Jupyter Notebook Experimentation
Open `model_experimentation.ipynb` in VS Code or Jupyter Notebook to inspect:
- 3D RGB pixel color distribution.
- **Elbow Curve Plot** ($\text{Inertia vs. } K$) to analyze optimal cluster selection.
- Subplots comparing $K=2, 4, 8, 16, 32$.

### Option 3: Docker Container
Run the containerized app with a single command:
```bash
docker compose up --build
```
Access the web app at `http://localhost:8000`.

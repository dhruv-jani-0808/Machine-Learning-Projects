# 🎬 Movie Recommendation System

This project recommends movies to users by analyzing historical ratings. It constructs a user-item rating matrix and implements the **K-Nearest Neighbors (KNN)** algorithm with Cosine Similarity to find similar movies based on user rating behaviors.

---

## 📊 Dataset

The dataset used in this project is the MovieLens Latest Small Dataset, containing user-generated movie ratings and tags.

* **Kaggle Link:** [MovieLens Latest Small Dataset](https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset)
* **Scale:** Contains **100,836 ratings** across **9,742 movies** created by **610 users**.
* **Dependent Variable (Target):** `rating` — The target values used to build the user-item rating matrix.

---

## 🛠️ Data Preprocessing & Pivoting

To build an efficient recommendation model, the following preprocessing steps are performed:

### 1. Merging & Filtering
* **Join:** Merges `movies.csv` and `ratings.csv` on the `movieId` key.
* **Popularity Filtering:** Group by movie `title` and calculate total ratings. Movies with fewer than **10 ratings** are filtered out to remove noise and ensure recommendations are based on sufficient user consensus.

### 2. Matrix Pivoting & Sparsity
* **User-Item Matrix:** Creates a pivot table (`movie_pivot`) with `title` as the index, `userId` as the columns, and `rating` as the cell values. Missing ratings are filled with `0`.
* **Sparse Matrix representation:** Since most users have only rated a small subset of movies, the pivot table is highly sparse. It is converted into a Compressed Sparse Row (CSR) matrix using `scipy.sparse.csr_matrix` to save memory and speed up computation.

---

## 🤖 Model & Recommendation Logic

* **Algorithm:** Unsupervised **K-Nearest Neighbors (KNN)** (`sklearn.neighbors.NearestNeighbors`).
* **Metric:** Cosine Similarity (`metric='cosine'`, `algorithm='brute'`) is used to measure the angle between movie rating vectors rather than absolute Euclidean distance.
* **Recommendation System:**
  * Clean and match the user's text query to find the target movie in the database.
  * Extract the row index of the target movie.
  * Query the KNN model for the `n_neighbors=6` closest vectors.
  * Output the top 5 closest matching movies (excluding the query movie itself) along with their similarity confidence percentages.

---

## 📈 Results & Visualization

* **Recommendations:**
  * Searching **"Toy Story"** yields highly relevant recommendations such as *Toy Story 2*, *Bug's Life, A*, *Toy Story 3*, and *Monsters, Inc.*.
  * Searching **"Matrix"** yields sci-fi classics and cyber-action movies like *Animatrix, The*, *Blade*, and *Hackers*.
* **Movie Universe Visualization:**
  * Compresses the 610 user-dimensions down to 2 principal components using Principal Component Analysis (PCA).
  * Plots the compressed coordinates of all catalog movies in a scatter plot.
  * Highlights clusters of different genres (Sci-Fi, Kids/Animation, and Highly-Rated Classics) to show how the KNN model groups movies visually.

---

## ⚙️ How to Run

1. Make sure you have the required libraries installed:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn scipy
   ```
2. Download the datasets from the [Kaggle Dataset Page](https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset) and place `movies.csv`, `ratings.csv`, `links.csv`, and `tags.csv` in the `Dataset/` directory.
3. Launch and run the Jupyter notebook:
   ```bash
   jupyter notebook movie_recommendation.ipynb
   ```

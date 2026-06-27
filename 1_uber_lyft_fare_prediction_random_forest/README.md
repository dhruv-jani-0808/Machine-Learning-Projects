# 🚗 Uber & Lyft Fare Price Predictor

This project predicts the fare price of Uber and Lyft rides in the Boston area by analyzing trip characteristics and local atmospheric weather conditions. It leverages a **Random Forest Regressor** to model non-linear interactions between travel patterns, surge pricing, and weather metrics.

---

## 📊 Dataset

The dataset used in this project is constructed by joining dynamic ride-hailing logs with meteorological weather logs. 

* **Kaggle Link:** [Uber and Lyft Cab Prices Dataset](https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices)
* **Scale:** After preprocessing, missing value handling, temporal feature engineering, and dummy encoding of categorical features, the final dataset contains **637,976 rows** and **37 columns**.
* **Dependent Variable (Target):** `price` (numerical fare value of the ride).

---

## 🛠️ Feature Engineering & Representation

The independent features are divided into two main categories:

### 1. Trip Characteristics
* `distance` — The trip distance in miles.
* `surge_multiplier` — Demand-based price multiplier (e.g. 1.0, 1.25, 1.5, 2.0).
* `cab_type` — Service provider (Uber or Lyft).
* `name` — Specific ride category (e.g., Shared, Lyft XL, Lux, Lux Black, UberPool, UberX, Black, Black SUV).
* `hour` & `day_of_week` — Temporal patterns extracted from timestamps to capture peak and off-peak behaviors.

### 2. Meteorological (Weather) Features
* `temp` — Local temperature in Fahrenheit.
* `clouds` — Percentage of cloud cover.
* `pressure` — Atmospheric pressure.
* `rain` — Rain volume in inches.
* `humidity` — Relative humidity percentage.
* `wind` — Wind speed.

---

## 🤖 Model & Training

* **Algorithm:** Supervised Regression using a **Random Forest Regressor** (`sklearn.ensemble.RandomForestRegressor`).
* **Hyperparameters:** Configured with `n_estimators=20` and `random_state=42` to strike a balance between performance and computational training time.
* **Train/Test Split:** Standard split to evaluate generalization performance on unseen ride observations.

---

## 📈 Results & Performance

The model shows high predictive capability:
* **Mean Absolute Error (MAE):** **$1.27**
* **R-squared ($R^2$) Score:** **95.68%**

This demonstrates that trip features, combined with high-quality demand signals (surge multipliers), are highly predictive of ride fare rates, while weather features play a minor but complementary role.

---

## ⚙️ How to Run

1. Make sure you have the required libraries installed:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```
2. Download the datasets from the [Kaggle Dataset Page](https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices) and place `cab_rides.csv` and `weather.csv` in the `Dataset/` directory.
3. Launch and run the Jupyter notebook:
   ```bash
   jupyter notebook uber_lyft_fare_prediction.ipynb
   ```

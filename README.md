# Machine Learning Projects

A curated portfolio of end-to-end Machine Learning projects focusing on data preprocessing, exploratory data analysis (EDA), predictive modeling, and model evaluation across various domains. 

Each project demonstrates a practical application of data science workflows, from cleaning and merging raw datasets to training, tuning, and evaluating statistical and machine learning models.

---

## 📋 List of Projects

### 1. Uber & Lyft Fare Price Predictor (Regression)
* **Folder:** [`1_random_forest_regression`](file:///d:/machine%20learning/Projects/1_random_forest_regression)
* **Goal:** Predicts the fare price of Uber and Lyft rides in the Boston area based on trip characteristics and atmospheric conditions.
* **Key Details:**
  * **Machine Learning Type:** Supervised Regression using a Random Forest Regressor (`sklearn.ensemble.RandomForestRegressor` with 20 estimators).
  * **Dataset & Scale:** Constructed by merging real-time ride data (`cab_rides.csv`) and local weather data (`weather.csv`). After handling missing values, temporal feature engineering, and dummy-encoding categorical features, the final processed dataset has **637,976 rows** and **37 columns**.
  * **Dependent Variable (Target):** `price` — The numeric fare of the cab ride.
  * **Independent Features:** 
    * *Trip features:* `distance` (miles), `surge_multiplier`, `cab_type` (Lyft/Uber brand), `name` (service type e.g., Shared, Lux, Lux Black XL, Lyft XL), `hour`, and `day_of_week`.
    * *Weather features:* `temp` (Fahrenheit), `clouds` (cloud cover), `pressure`, `rain` (inches), `humidity`, and `wind` speed.
  * **Model Performance:** Achieved a **Mean Absolute Error (MAE) of $1.27** and an **R-squared ($R^2$) score of 95.68%**.

---

### 2. E-Commerce Customer Churn Predictor (Classification)
* **Folder:** [`2_logistic_regression`](file:///d:/machine%20learning/Projects/2_logistic_regression)
* **Goal:** Predicts customer churn (whether a customer will stop using the e-commerce platform) based on demographics, purchase history, satisfaction metrics, and app engagement.
* **Key Details:**
  * **Machine Learning Type:** Supervised Binary Classification using Logistic Regression (`sklearn.linear_model.LogisticRegression` with L2 regularization).
  * **Dataset & Scale:** Uses `E Commerce Dataset.xlsx` consisting of **5,630 rows** and **20 features** (demographics, transactional history, and app engagement). After scaling and one-hot encoding categorical features, the final dataset contains **26 columns**.
  * **Dependent Variable (Target):** `Churn` — Binary classification label (1 if the customer churned/left the platform, 0 if they stayed).
  * **Independent Features:**
    * *Customer Profile:* `Tenure` (months active), `Gender`, `MaritalStatus`, `CityTier`, and `NumberOfAddress`.
    * *App Engagement:* `PreferredLoginDevice`, `HourSpendOnApp`, and `NumberOfDeviceRegistered`.
    * *Purchase & Payment Behavior:* `PreferredPaymentMode`, `PreferedOrderCat` (e.g. Laptop & Accessory, Mobile, Fashion), `OrderCount`, `DaySinceLastOrder`, `OrderAmountHikeFromlastYear`, `CouponUsed`, and `CashbackAmount`.
    * *Satisfaction & Complaints:* `SatisfactionScore` (1-5 scale) and `Complain` (1 if customer raised a complaint, 0 otherwise).
  * **Threshold Optimization:** Lowered decision threshold from `0.5` to `0.35` to minimize costly False Negatives (missing churners), increasing correct churn detection (True Positives) from **110 to 130** (a 26.7% reduction in False Negatives).
  * **Model Performance:** Achieved a **ROC AUC Score of 0.8981**.

---

## 🛠️ Requirements & Setup

To explore and run the Jupyter notebooks in this repository:

1. **Install Dependencies:**
   Make sure you have Python installed, then install the necessary scientific libraries:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

2. **Run Notebooks:**
   Launch Jupyter Notebook or JupyterLab and open the `main.ipynb` or the `.ipynb` files in the respective project directories:
   ```bash
   jupyter notebook
   ```

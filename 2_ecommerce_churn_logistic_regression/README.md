# 🛒 E-Commerce Customer Churn Predictor

This project predicts customer churn (whether a customer will stop using an e-commerce platform) based on demographics, purchase history, satisfaction metrics, and app engagement. It leverages a **Logistic Regression** model optimized specifically for business decision-making.

---

## 📊 Dataset

The dataset represents user behavior on a leading e-commerce platform.

* **Kaggle Link:** [E-Commerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)
* **Scale:** The raw data consists of **5,630 rows** and **20 features**. After standard scaling of numeric variables and one-hot encoding of categorical features, the final dataset contains **26 columns**.
* **Dependent Variable (Target):** `Churn` (binary classification label: `1` if the customer churned, `0` otherwise).

---

## 🛠️ Feature Engineering & Representation

The independent features are divided into four main domains:

### 1. Customer Profile
* `Tenure` — Number of months active.
* `Gender` & `MaritalStatus`.
* `CityTier` & `NumberOfAddress`.

### 2. App Engagement
* `PreferredLoginDevice` — Mobile Phone, Computer, etc.
* `HourSpendOnApp` — Hours spent daily on the application.
* `NumberOfDeviceRegistered` — Number of devices registered under the account.

### 3. Purchase & Payment Behavior
* `PreferredPaymentMode` — Debit/Credit Card, UPI, Cash on Delivery, etc.
* `PreferedOrderCat` — Preferred shopping category (e.g. Laptop & Accessory, Mobile, Fashion, Grocery).
* `OrderCount`, `DaySinceLastOrder`, `OrderAmountHikeFromlastYear`.
* `CouponUsed`, `CashbackAmount`.

### 4. Satisfaction & Complaints
* `SatisfactionScore` — Numeric score rating (1 to 5).
* `Complain` — Binary flag representing whether a customer raised a formal complaint in the last month.

---

## 🤖 Model & Optimization

* **Algorithm:** Supervised Binary Classification using **Logistic Regression** (`sklearn.linear_model.LogisticRegression` with L2 regularization).
* **Threshold Optimization:** In customer retention, missing a customer who is about to churn (a False Negative) is much more expensive than giving a promotion to a loyal customer (a False Positive). 
  * To minimize False Negatives, the classification decision threshold was lowered from **`0.5`** to **`0.35`**.
  * This increased correct churn detections (True Positives) from **110 to 130** (a 26.7% reduction in False Negatives).

---

## 📈 Results & Performance

* **ROC AUC Score:** **0.8981**
* The classification threshold optimization significantly boosted sensitivity (Recall) for the churn class, aligning the model with realistic business goals (churn mitigation).

---

## ⚙️ How to Run

1. Make sure you have the required libraries installed:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn openpyxl
   ```
   *(Note: `openpyxl` is required for loading Excel files)*
2. Download the dataset from the [Kaggle Dataset Page](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction) and place `E Commerce Dataset.xlsx` in the `Dataset/` directory.
3. Launch and run the Jupyter notebook:
   ```bash
   jupyter notebook ecommerce_churn_prediction.ipynb
   ```

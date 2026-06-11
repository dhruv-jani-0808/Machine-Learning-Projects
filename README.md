# Machine Learning Projects

A curated portfolio of end-to-end Machine Learning projects focusing on data preprocessing, exploratory data analysis (EDA), predictive modeling, and model evaluation across various domains. 

Each project demonstrates a practical application of data science workflows, from cleaning and merging raw datasets to training, tuning, and evaluating statistical and machine learning models.

---

## 📋 List of Projects

### 1. Cab Ride Price Prediction (Regression)
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

### 2. Loan Default Risk Prediction (Classification)
* **Folder:** [`random_forest_classification`](file:///d:/machine%20learning/Projects/random_forest_classification)
* **Goal:** Classifies whether a borrower will fully pay back a LendingClub loan or default, enabling lenders to gauge underwriting risk.
* **Key Details:**
  * **Machine Learning Type:** Supervised Binary Classification using a Random Forest Classifier (`sklearn.ensemble.RandomForestClassifier` with 600 estimators).
  * **Dataset & Scale:** Uses `loan_data.csv` consisting of **9,578 borrower records** with **14 raw financial features**.
  * **Dependent Variable (Target):** `not.fully.paid` — Binary classification label (1 if the borrower defaulted/did not fully pay back, 0 if they successfully repaid the loan).
  * **Independent Features:**
    * *Credit Profile:* `credit.policy` (1 if borrower meets underwriting criteria, 0 otherwise), `fico` (FICO credit score), and `days.with.cr.line` (duration of borrower's credit line in days).
    * *Loan Terms:* `purpose` (loan purpose e.g., credit card, debt consolidation, educational, major purchase), `int.rate` (interest rate as a decimal), and `installment` (monthly payment due).
    * *Financial Health:* `log.annual.inc` (natural log of self-reported annual income), `dti` (debt-to-income ratio), `revol.bal` (unpaid revolving balance), and `revol.util` (revolving line utilization rate).
    * *Credit/Delinquency History:* `inq.last.6mths` (creditor inquiries in the last 6 months), `delinq.2yrs` (times delinquent on payments by 30+ days in the last 2 years), and `pub.rec` (number of derogatory public records).

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

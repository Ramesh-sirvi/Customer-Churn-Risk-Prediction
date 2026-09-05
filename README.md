E-Commerce Customer Churn Risk Prediction

📌 About the Project

This project predicts whether an e-commerce customer is at high risk of churn using machine learning.

The dataset contains 50,000 customers and 53 features.

🎯 Objective

The main goal is to identify customers who are likely to churn so that businesses can take action to improve customer retention.

🔧 Steps Performed

Loaded and explored the dataset

Checked missing values and duplicates

Created a binary churn-risk target

Removed data-leakage features

Encoded categorical data

Scaled numerical features

Handled class imbalance using SMOTE

Trained multiple machine learning models

Compared model performance

Analyzed important features

🤖 Models Used

Logistic Regression

Decision Tree

Random Forest

XGBoost

LightGBM

📊 Evaluation Metrics

The models are evaluated using:

Accuracy

Precision

Recall

F1-Score

ROC-AUC

🛠️ Technologies

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Imbalanced-learn

XGBoost

LightGBM

Jupyter Notebook

📁 Project Structure

E-Commerce-Churn-Risk-Prediction/
│
├── Churn_risk_prediction.ipynb
├── E-commerce_Customer_Segmentation_2026.csv
├── churn_predict_model.pkl
└── README.md

🚀 How to Run

1. Install the required libraries

pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost lightgbm jupyter

2. Place the dataset

Keep E-commerce_Customer_Segmentation_2026.csv in the project folder.

3. Open the notebook

jupyter notebook

Then open:

Churn_risk_prediction.ipynb

Run the cells from top to bottom.

💼 Business Use

The model can help businesses identify high-risk customers and target them with retention strategies such as personalized offers, discounts, or customer support.

👨‍💻 Author

Ramesh Choudhary


# 🚢 Titanic Survival Prediction — Machine Learning Project  

> 🧠 A complete Data Science project built from scratch — from Data Cleaning to Model Deployment using Streamlit.

---

## 🏆 Project Overview  

This project aims to predict whether a passenger survived the **Titanic shipwreck** using machine learning.  
I explored, analyzed, and visualized the dataset, then built predictive models to understand which factors most influenced survival.

---

## 📊 Key Highlights  

- 🔍 **Performed Exploratory Data Analysis (EDA)** using Seaborn & Matplotlib.  
- 🧹 **Handled missing values** and created meaningful **new features**.  
- ⚙️ **Trained multiple machine learning models** (Logistic Regression, Random Forest, etc.).  
- 💾 **Saved model pipeline** using `joblib`.  
- 🌐 **Deployed interactive web app** with Streamlit for real-time predictions.  

---

## 🧰 Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| Programming | Python 🐍 |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Deployment | Streamlit |
| Model Saving | Joblib |

---


---

## 🚀 Workflow  

1. **Data Understanding & Cleaning**
   - Removed irrelevant columns
   - Filled missing values (age, embarked, etc.)
   - Encoded categorical variables (`sex`, `embarked`)

2. **Exploratory Data Analysis**
   - Visualized survival rate by class, gender, and age
   - Discovered correlations and key influencing factors

3. **Feature Engineering**
   - Created new features like `family_size`, `is_alone`, and `fare_per_person`

4. **Model Building**
   - Used **Scikit-learn Pipelines** for preprocessing + model training  
   - Compared Logistic Regression, Random Forest, and XGBoost

5. **Evaluation**
   - Measured performance using accuracy, confusion matrix, and ROC-AUC

6. **Deployment**
   - Built a simple **Streamlit web app** to input passenger data and get survival predictions

---

## 📈 Results  

| Model | Accuracy | ROC-AUC |
|--------|-----------|---------|
| Logistic Regression | 79.8% | 0.84 |
| Random Forest | 83.2% | 0.88 |
| XGBoost | 84.7% | 0.90 |

✅ **Random Forest** performed best and was selected for deployment.

---




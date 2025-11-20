# 🧠 AI-Based Student Mental Stress Prediction System
### Predicting stress using Machine Learning + Behavioral & Academic Indicators  
🚀 Built using **Python, Scikit-Learn, XGBoost & Streamlit**

---

## 📌 Overview

Student mental stress is a growing concern, often driven by academic load, lack of sleep, and performance pressure.  
This project builds a **machine-learning powered stress prediction system** using real student datasets and deploys it as an interactive **Streamlit web app**.

The model predicts:

- 🔢 **Stress Score (1–5)** — using Random Forest Regression  
- 🏷 **Stress Category** — using XGBoost Classification  
- 🎯 **Personalized Recommendation**  

The app provides a **beautiful dashboard** with:

- Feature importance  
- Stress distribution  
- Correlation heatmap  
- Relationship plots  
- Model comparison charts  

---

## 🎯 Project Objectives

✔ To combine multiple real-world student stress datasets  
✔ To clean, standardize, and merge them into a unified dataset  
✔ To perform full EDA (correlation, distributions, relationships)  
✔ To apply feature engineering for improved prediction performance  
✔ To train & evaluate multiple ML models (Regression + Classification)  
✔ To compare all models based on R², RMSE, and Accuracy  
✔ To select the best model for deployment  
✔ To deploy a real-time stress prediction system using Streamlit  

---

## 🗂 Dataset Information

Two datasets were merged:

1. **Student Stress Factors Dataset**  
2. **Google Form Stress Survey Dataset**

After cleaning & preprocessing:

- Converted all features to **1–5 scale**  
- Mapped stress levels **Low → 1**, **Medium → 3**, **High → 5**  
- Removed missing/unmapped entries  
- Final combined file:  
  **`Combined_Student_Stress.csv` (≈ 400+ rows)**

---

## 🧪 Machine Learning Models Used

### **Regression Models**
| Model | Purpose |
|-------|---------|
| Simple Linear Regression | Baseline using single feature |
| Multiple Linear Regression | Multi-feature linear model |
| Polynomial Regression (Degree 2) | Captures non-linear trend |
| Decision Tree Regression | Tree-based stress scoring |
| 🌟 **Random Forest Regression** | ⭐ Best regression model (R² ≈ 0.68) |

### **Classification Models**
| Model | Purpose |
|-------|---------|
| Logistic Regression | Basic binary stress classification |
| KNN Classifier | Distance-based prediction |
| Naive Bayes | Probabilistic classifier |
| SVM | Margin-based classification |
| 🌟 **XGBoost Classifier** | ⭐ Best classifier (Accuracy ≈ 0.86) |

---

## ⭐ Final Models Used in Deployment

| Task | Model | Reason |
|------|-------|--------|
| **Stress Score Prediction** | Random Forest Regressor | Highest accuracy, low RMSE |
| **Stress Category Prediction** | XGBoost Classifier | Best multi-class performance |

---

## 🖥 Streamlit Web App Features

### 🎛 **Input Section**
- Sleep quality  
- Academic performance  
- Study load  
- Extracurricular load  

### 📊 **Output**
- Predicted Stress Score  
- Stress Category  
- Personalized recommendations  

### 📈 **Interactive Dashboard**
- Random Forest Feature Importance  
- Stress Level Distribution  
- Correlation Heatmap  
- Scatter plots  
- Box plots  
- Model comparison bar charts  
- Mini pairplot  

---

Check 
# 🧠 AI-Based Student Mental Stress Prediction System
### Predicting stress using Machine Learning + Behavioral & Academic Indicators  
🚀 Built using **Python, Scikit-Learn, XGBoost & Streamlit**

---

## 📌 Overview

Student mental stress is a growing concern, often driven by academic load, lack of sleep, and performance pressure.  
This project builds a **machine-learning powered stress prediction system** using real student datasets and deploys it as an interactive **Streamlit web app**.

The model predicts:

- 🔢 **Stress Score (1–5)** — using Random Forest Regression  
- 🏷 **Stress Category** — using XGBoost Classification  
- 🎯 **Personalized Recommendation**  

The app provides a **beautiful dashboard** with:

- Feature importance  
- Stress distribution  
- Correlation heatmap  
- Relationship plots  
- Model comparison charts  

---

## 🎯 Project Objectives

✔ **To combine** multiple real-world student stress datasets  
✔ **To clean, standardize, and merge** them into a unified dataset  
✔ **To perform full EDA** (correlation, distributions, relationships)  
✔ **To apply feature engineering** for improved prediction performance  
✔ **To train & evaluate** multiple ML models (Regression + Classification)  
✔ **To compare** all models based on R², RMSE, and Accuracy  
✔ **To select the best model** for deployment  
✔ **To deploy** a real-time stress prediction system using Streamlit  

---

## 🗂 Dataset Information

Two datasets were merged:

1. **Student Stress Factors Dataset**  
2. **Google Form Stress Survey Dataset**

After cleaning & preprocessing:

- Converted all features to **1–5 scale**  
- Mapped stress levels **Low → 1**, **Medium → 3**, **High → 5**  
- Removed missing/unmapped entries  
- Final combined file:  
  **`Combined_Student_Stress.csv` (≈ 400+ rows)**

---

## 🧪 Machine Learning Models Used

### **Regression Models**
| Model | Purpose |
|-------|---------|
| Simple Linear Regression | Baseline using single feature |
| Multiple Linear Regression | Multi-feature linear model |
| Polynomial Regression (Degree 2) | Captures non-linear trend |
| Decision Tree Regression | Tree-based stress scoring |
| 🌟 **Random Forest Regression** | ⭐ Best regression model (R² ≈ 0.68) |

### **Classification Models**
| Model | Purpose |
|-------|---------|
| Logistic Regression | Basic binary stress classification |
| KNN Classifier | Distance-based prediction |
| Naive Bayes | Probabilistic classifier |
| SVM | Margin-based classification |
| 🌟 **XGBoost Classifier** | ⭐ Best classifier (Accuracy ≈ 0.86) |

---

## ⭐ Final Models Used in Deployment

| Task | Model | Reason |
|------|-------|--------|
| **Stress Score Prediction** | Random Forest Regressor | Highest accuracy, low RMSE |
| **Stress Category Prediction** | XGBoost Classifier | Best multi-class performance |

---

## 🖥 Streamlit Web App Features

### 🎛 **Input Section**
- Sleep quality  
- Academic performance  
- Study load  
- Extracurricular load  

### 📊 **Output**
- Predicted Stress Score  
- Stress Category  
- Personalized recommendations  

### 📈 **Interactive Dashboard**
- Random Forest Feature Importance  
- Stress Level Distribution  
- Correlation Heatmap  
- Model comparison bar charts  

---


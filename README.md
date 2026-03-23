# 🚀 Heart Failure Prediction System (PySpark + Tableau)

## 📌 Project Overview
This project presents an end-to-end data analytics and machine learning pipeline for heart failure prediction using **PySpark** and interactive visualization using **Tableau**.

The system processes clinical data, applies multiple machine learning models, and visualizes insights through dashboards to support healthcare decision-making.

---

## ⚙️ Technologies Used
- **PySpark (Apache Spark)** – Big data processing and ML pipeline  
- **Python** – Programming and scripting  
- **Spark MLlib** – Machine learning models  
- **Tableau** – Interactive dashboards and visualization  
- **Scikit-learn** – Model comparison  

---

## 📂 Dataset
Clinical dataset containing:
- Age  
- Anaemia  
- Diabetes  
- High blood pressure  
- Serum creatinine  
- Smoking  
- Death event (target variable)  

---

## 🔄 PySpark Pipeline

### Data Processing
- Loaded dataset using Spark  
- Handled missing values  
- Cached dataset for performance  

### Feature Engineering
- VectorAssembler for feature creation  
- StandardScaler for normalization  

### Model Training
- Logistic Regression  
- Random Forest  
- Decision Tree  
- Gradient Boosted Trees  

### Model Evaluation
- BinaryClassificationEvaluator used  
- Compared model performance  

### Hyperparameter Tuning
- Cross-validation on Random Forest  
- Tuned number of trees and depth  

---

## 📊 Tableau Dashboards

### 1️⃣ Demographic Overview
- Age, sex, smoking, and blood pressure distribution  

### 2️⃣ Mortality Analysis
- Death vs survival distribution  

### 3️⃣ Age vs Mortality Risk
- Impact of age on death probability  

### 4️⃣ Clinical Factors Impact
- Diabetes, anaemia, and hypertension analysis  

---

## 📈 Key Insights
- Older patients (60+) have higher mortality risk  
- Diabetes and high blood pressure significantly affect survival  
- Dataset shows imbalance in death events  
- Ensemble models (Random Forest, GBT) perform better  

---

## 🚀 How to Run

### Using Python
```bash
python run_pipeline.py
```

### Using Docker
```bash
docker build -t heart-failure-app .
docker run heart-failure-app
```

### Tableau
- Open `.twbx` file in Tableau  
- Explore dashboards interactively  

---

## 🎯 Objective
To demonstrate the integration of **big data processing (PySpark)** and **data visualization (Tableau)** for healthcare analytics and predictive modeling.

---

## 📌 Future Improvements
- Deploy model using APIs  
- Add real-time data processing  
- Enhance dashboard interactivity  
- Integrate deep learning models  

---

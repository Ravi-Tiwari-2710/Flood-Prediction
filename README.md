# Flood Prediction & Early Warning System 🌊⚠️

A machine learning based predictive system designed to analyze historical rainfall patterns and provide early warnings for potential flood disasters.

## 🌟 Key Features

- **Rainfall Pattern Analysis:** Analyzes monthly rainfall data to identify trends and anomalies that lead to flooding.
- **Predictive Modeling:** Utilizes a **Random Forest Classifier** to predict the probability of a flood based on historical data.
- **Automated Early Warning:** Integrated with a notification API to send real-time alerts to authorities and citizens when flood risk exceeds a critical threshold.
- **Probability Scoring:** Instead of a simple Yes/No, the system provides a probability percentage for more nuanced risk assessment.

## 🛠️ Technical Architecture

### 1. The Prediction Pipeline
`Historical Data (CSV)` $\rightarrow$ `Feature Engineering` $\rightarrow$ `Random Forest Model` $\rightarrow$ `Risk Probability` $\rightarrow$ `Notification API`.

### 2. Tech Stack
- **Language:** Python 3.x
- **ML Libraries:** Scikit-learn, Pandas, NumPy
- **Model Persistence:** Joblib
- **Alerting:** Requests (MyNotifier API)

## 🚀 Getting Started

### Installation
```bash
git clone https://github.com/Ravi-Tiwari-2710/Flood-Prediction.git
pip install pandas scikit-learn joblib requests
```

### Usage
```bash
python main.py
```

## 📈 Impact & Vision
This system aims to reduce the loss of life and property by providing critical lead time for evacuations and disaster management. By integrating real-time weather API data, the system can be evolved into a live regional monitoring dashboard.

---
*Developed by [Ravi Tiwari](https://github.com/Ravi-Tiwari-2710)*

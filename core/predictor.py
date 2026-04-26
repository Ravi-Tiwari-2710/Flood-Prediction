import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

class FloodPredictor:
    """Professional Flood Prediction system using ML."""
    def __init__(self, model_path='models/flood_model.pkl'):
        self.model_path = model_path
        self.model = self._load_or_train_model()

    def _load_or_train_model(self):
        if os.path.exists(self.model_path):
            return joblib.load(self.model_path)
        
        print("Model not found. Training a new Random Forest model...")
        # Load dataset
        df = pd.read_csv('data/kerala.csv')
        
        # Feature Engineering
        # In this dataset, we use rainfall patterns. 
        # We define a 'Flood' as cases where June-Sept rainfall is significantly above average.
        # Since this is a historical dataset without labels, we create labels based on a threshold.
        threshold = df['Jun-Sep'].mean() + 1.5 * df['Jun-Sep'].std()
        df['Flood'] = (df['Jun-Sep'] > threshold).astype(int)
        
        # Select features: Monthly rainfall
        features = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        X = df[features]
        y = df['Flood']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Model: Random Forest for robustness
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        print(f"Model trained. Accuracy: {accuracy_score(y_test, model.predict(X_test)):.2f}")
        
        # Save model
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(model, self.model_path)
        
        return model

    def predict(self, rainfall_data):
        """
        Predicts flood possibility.
        :param rainfall_data: List of 12 monthly rainfall values.
        """
        data = np.array(rainfall_data).reshape(1, -1)
        prediction = self.model.predict(data)
        probability = self.model.predict_proba(data)[0][1]
        
        return {
            'flood_risk': bool(prediction[0]),
            'probability': round(probability * 100, 2)
        }

class FloodNotifier:
    """Handles alerts for predicted floods."""
    def __init__(self, api_key='48f21a98-f24f-42c7-b984-fae70e8aa3b9'):
        self.api_key = api_key
        self.api_url = 'http://api.mynotifier.app'

    def send_alert(self, probability):
        import requests
        payload = {
            "apiKey": self.api_key,
            "message": "⚠️ FLOOD ALERT!",
            "description": f"High risk of flood detected. Probability: {probability}%",
            "type": "warning",
        }
        try:
            response = requests.post(self.api_url, data=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Notification failed: {e}")
            return False

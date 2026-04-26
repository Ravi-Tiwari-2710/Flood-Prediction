import os
from core.predictor import FloodPredictor, FloodNotifier

def main():
    # Initialize components
    predictor = FloodPredictor()
    notifier = FloodNotifier()
    
    # Example: Current year's hypothetical rainfall data (JAN to DEC)
    # Using average values for demonstration
    current_rainfall = [25.0, 30.0, 45.0, 100.0, 180.0, 900.0, 800.0, 400.0, 250.0, 300.0, 350.0, 50.0]
    
    print("Analyzing rainfall patterns...")
    result = predictor.predict(current_rainfall)
    
    if result['flood_risk']:
        print(f"🚨 ALERT: High Flood Risk detected! Probability: {result['probability']}%")
        success = notifier.send_alert(result['probability'])
        if success:
            print("Notification sent successfully.")
        else:
            print("Failed to send notification.")
    else:
        print(f"✅ Safe: Low flood risk. Probability: {result['probability']}%")

if __name__ == "__main__":
    main()

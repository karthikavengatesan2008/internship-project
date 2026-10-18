import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

print("Starting Model Training...")

# Generate dummy dataset for Gearbox Sensors
np.random.seed(42)
data_size = 1000
df = pd.DataFrame({
    'Vibration_X': np.random.normal(5, 3, data_size),
    'Vibration_Y': np.random.normal(5, 3, data_size),
    'Vibration_Z': np.random.normal(5, 3, data_size),
    'Temperature': np.random.normal(60, 15, data_size),
    'Status': np.random.choice([0, 1], size=data_size) # 0: Healthy, 1: Faulty
})

# Feature selection
X = df[['Vibration_X', 'Vibration_Y', 'Vibration_Z', 'Temperature']]
y = df['Status']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Logistic Regression Model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_acc = accuracy_score(y_test, lr_model.predict(X_test))
print(f"Logistic Regression Accuracy: {lr_acc:.2f}")

# 2. Random Forest Model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf_model.predict(X_test))
print(f"Random Forest Accuracy: {rf_acc:.2f}")

# Save the best model
joblib.dump(rf_model, 'random_forest_model.pkl')
print("Random Forest Model saved as 'random_forest_model.pkl'")

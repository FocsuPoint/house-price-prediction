# ==========================================
# House Price Prediction - Model Training
# ==========================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os


# ==========================================
# 1. Load Dataset
# ==========================================

print("Loading dataset...")

data = pd.read_csv("data/train.csv")

print("Dataset loaded successfully!")
print("Rows:", len(data))
print("Columns:", list(data.columns))


# ==========================================
# 2. Select Features
# ==========================================

features = [
    "GrLivArea",
    "YearBuilt",
    "GarageCars",
    "TotalBsmtSF",
    "OverallQual",
    "OverallCond"
]

target = "SalePrice"


X = data[features]
y = data[target]


# ==========================================
# 3. Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 4. Create Machine Learning Model
# ==========================================

print("\nTraining Linear Regression model...")

model = LinearRegression()

model.fit(X_train, y_train)

print("Model trained successfully!")


# ==========================================
# 5. Make Predictions
# ==========================================

predictions = model.predict(X_test)


# ==========================================
# 6. Evaluate Model
# ==========================================

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = mse ** 0.5

r2 = r2_score(y_test, predictions)


print("\n==========================================")
print("MODEL PERFORMANCE")
print("==========================================")

print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R²  :", round(r2, 4))


# ==========================================
# 7. Create Model Folder
# ==========================================

os.makedirs("model", exist_ok=True)


# ==========================================
# 8. Save Trained Model
# ==========================================

model_path = "model/house_price_model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Location:", model_path)


# ==========================================
# 9. Test Prediction
# ==========================================

sample_house = pd.DataFrame([{
    "GrLivArea": 1800,
    "YearBuilt": 2010,
    "GarageCars": 2,
    "TotalBsmtSF": 900,
    "OverallQual": 7,
    "OverallCond": 6
}])

sample_prediction = model.predict(sample_house)[0]


print("\n==========================================")
print("SAMPLE HOUSE PREDICTION")
print("==========================================")

print("Estimated Price: ₹", round(sample_prediction, 2))

print("\nTraining process completed!")

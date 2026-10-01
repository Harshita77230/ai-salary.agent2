import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib


data = pd.read_csv("data/ds_salaries.csv", engine="python")


# Only the five features exposed in the UI.
# remote_ratio is numeric (0 / 50 / 100) — no LabelEncoder needed.
categorical_cols = [
    "experience_level",
    "job_title",
    "company_location",
    "company_size",
]

encoder = {}

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoder[col] = le


feature_cols = [
    "experience_level",
    "job_title",
    "company_location",
    "company_size",
    "remote_ratio",
]

X = data[feature_cols]
y = data["salary_in_usd"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
)


model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score  = model.score(X_test,  y_test)
print(f"Train R²: {train_score:.4f}   Test R²: {test_score:.4f}")


joblib.dump(model,   "model/salary_model.pkl")
joblib.dump(encoder, "model/encoder.pkl")

print("Model saved.")

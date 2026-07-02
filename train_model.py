import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib


data = pd.read_csv("data/ds_salaries.csv", engine="python")


columns = [
"experience_level",
"employment_type",
"job_title",
"company_location",
"company_size",
"remote_ratio"
]


encoder = {}

for col in columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoder[col] = le


X = data[columns]
y = data["salary_in_usd"]


X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


model.fit(X_train,y_train)


joblib.dump(model,"model/salary_model.pkl")
joblib.dump(encoder,"model/encoder.pkl")


print("Model Saved")
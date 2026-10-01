import streamlit as st
import joblib
import pandas as pd


model=joblib.load("model/salary_model.pkl")
encoder=joblib.load("model/encoder.pkl")


st.title("AI Salary Prediction Agent")


experience=st.selectbox(
"Experience",
encoder["experience_level"].classes_
)


job=st.selectbox(
"Job Role",
encoder["job_title"].classes_
)


company=st.selectbox(
"Company Size",
encoder["company_size"].classes_
)


location=st.selectbox(
"Location",
encoder["company_location"].classes_
)


remote=st.number_input(
"Remote Ratio",
0,100,50
)


if st.button("Predict"):

    input_data=pd.DataFrame({

    "experience_level":
    [encoder["experience_level"].transform([experience])[0]],

    "employment_type":[0],

    "job_title":
    [encoder["job_title"].transform([job])[0]],

    "company_location":
    [encoder["company_location"].transform([location])[0]],

    "company_size":
    [encoder["company_size"].transform([company])[0]],

    "remote_ratio":[remote]

    })


    salary=model.predict(input_data)[0]


    st.success(
    f"Predicted Salary: ${salary:.2f}"
    )

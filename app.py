import pickle
import streamlit as st


df = pickle.load(open("diabetes_model.pkl","rb"))

st.title("Diabetes Prediction using ML")

Pregnancies = st.text_input("Number of Pregnancies")
Glucose = st.text_input("Glucose level")
BloodPressure= st.text_input("Blood Pressure value")
SkinThickness = st.text_input("Skin Thickness value")
Insulin= st.text_input("Insulin value")
BMI = st.text_input("BMI value")
DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
Age = st.text_input("Enter the age")

dia_diagnose = ""

#Creating button for prediction
if st.button("Predict"):
    dia_prediction = df.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if dia_prediction[0] == 1:
        dia_diagnose = "The person is Diabetic"
    else:
        dia_diagnose = "The person is Not Diabetic"
st.success(dia_diagnose)



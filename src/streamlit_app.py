import streamlit as st
import joblib
import pandas as pd

# 1. Load your pipeline
model = joblib.load('student_model_pipeline.joblib')

st.title("🎓 Student Exam Score Predictor")
st.write("Enter student details below to predict the final exam score.")

# 2. Create the UI Layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=15, max_value=30, value=20)
    study_hours = st.slider("Study Hours per Day", 0.0, 20.0, 8.0)
    attendance = st.slider("Class Attendance (%)", 0.0, 100.0, 90.0)
    sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0)

with col2:
    gender = st.selectbox("Gender", ["female", "male", "other"])
    course = st.selectbox("Course", ["b.sc", "bca", "diploma"])
    internet = st.radio("Internet Access", ["yes", "no"])
    method = st.selectbox("Study Method", ["self-study", "online videos", "coaching", "group study"])

# 3. Handle the prediction
if st.button("Predict Score"):
    # Create the dataframe exactly like the model expects
    input_data = pd.DataFrame([{
        "age": age, "study_hours": study_hours, "class_attendance": attendance,
        "sleep_hours": sleep, "gender": gender, "course": course,
        "internet_access": internet, "study_method": method,
        "sleep_quality": "average", "facility_rating": "medium", "exam_difficulty": "moderate"
    }])
    
    prediction = model.predict(input_data)[0]
    st.success(f"### Predicted Exam Score: {prediction:.2f}")
import streamlit as st
import pandas as pd
import joblib

# Load the trained Logistic Regression model
logreg_model = joblib.load('/content/logistic_regression_model.pkl')

# Define the Streamlit app
def main():
    st.title('Ten-Year CHD Risk Prediction')
    st.write('Enter patient information to predict Ten-Year CHD Risk.')

    # Create a form for user input
    age = st.sidebar.slider('Age', 20, 100, 50)
    male = st.sidebar.radio('Gender', ['Female', 'Male'])
    education = st.sidebar.slider('Education', 1, 5, 3)
    current_smoker = st.sidebar.radio('Current Smoker', ['No', 'Yes'])
    cigs_per_day = st.sidebar.slider('Cigarettes Per Day', 0, 70, 20)
    bp_meds = st.sidebar.radio('BPMeds', ['No', 'Yes'])
    prevalent_stroke = st.sidebar.radio('Prevalent Stroke', ['No', 'Yes'])
    prevalent_hyp = st.sidebar.radio('Prevalent Hypertension', ['No', 'Yes'])
    diabetes = st.sidebar.radio('Diabetes', ['No', 'Yes'])
    tot_chol = st.sidebar.slider('Total Cholesterol', 100, 600, 200)
    sys_bp = st.sidebar.slider('Systolic Blood Pressure', 80, 300, 120)
    dia_bp = st.sidebar.slider('Diastolic Blood Pressure', 40, 150, 80)
    bmi = st.sidebar.slider('BMI', 15.0, 40.0, 25.0)
    heart_rate = st.sidebar.slider('Heart Rate', 40, 150, 75)
    glucose = st.sidebar.slider('Glucose', 40, 400, 100)

    # Create a DataFrame with the user input
    gender = 1 if male == 'Male' else 0
    smoker = 1 if current_smoker == 'Yes' else 0
    bp_meds_value = 1 if bp_meds == 'Yes' else 0
    stroke = 1 if prevalent_stroke == 'Yes' else 0
    hypertension = 1 if prevalent_hyp == 'Yes' else 0
    diabetes_value = 1 if diabetes == 'Yes' else 0

    user_input = pd.DataFrame({
        'male': [gender],
        'age': [age],
        'education': [education],
        'currentSmoker': [smoker],
        'cigsPerDay': [cigs_per_day],
        'BPMeds': [bp_meds_value],
        'prevalentStroke': [stroke],
        'prevalentHyp': [hypertension],
        'diabetes': [diabetes_value],
        'totChol': [tot_chol],
        'sysBP': [sys_bp],
        'diaBP': [dia_bp],
        'BMI': [bmi],
        'heartRate': [heart_rate],
        'glucose': [glucose]
    })

    # Add a predict button
    if st.sidebar.button('Predict'):
        # Make prediction
        prediction = logreg_model.predict(user_input)[0]
        if prediction == 1:
            result = 'High Risk'
        else:
            result = 'Low Risk'

        # Display prediction result
        st.write(f'Ten-Year CHD Risk: {result}')

if __name__ == '__main__':
    main()

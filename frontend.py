import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/predict'

st.title('Insurance Category Prediction')

st.markdown('Enter your details below : ')

age = st.number_input("Age", min_value=1, max_value=120, value = 30) 
weight = st.number_input("Weight (kg)", min_value=1.0, value = 65.0) 
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value = 1.7) 
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value = 10.0) 
smoker = st.selectbox("Are you a smoker ?", options = [True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox("Occupation", ['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])

if st.button("Predit Category"):
       input_data = {
              'age' : age,
              'weight' : weight,
              'height' : height,
              'income_lpa' : income_lpa,
              'smoker' : smoker,
              'city' : city,
              'occupation' : occupation
       }

       try:
              respone = requests.post(API_URL, json=input_data)
              if respone.status_code == 200:
                     result = respone.json()
                     st.success(f'Predicted Category : **{result['predicted_category']}**')
              else: 
                     st.error(f'API Error : {respone.status_code} - {respone.text}')
       except requests.exceptions.ConnectionError:
              st.error('Could not connect to FastAPI Server, make sure you are running it on port 8000')



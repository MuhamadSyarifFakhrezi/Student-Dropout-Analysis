import pandas as pd
import numpy as np
import joblib
import streamlit as st
from st_pages import add_page_title
import time


X = ['Application_mode', 'Course', 'Fathers_qualification', 'Mothers_qualification', 'Fathers_occupation', 'Mothers_occupation', 'Scholarship_holder',
     'Tuition_fees_up_to_date', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_approved',
     'Curricular_units_2nd_sem_grade']

encoders = {}
for feature in X[:6]:
  encoders[f'{feature}_encoder'] = joblib.load(f'model/{feature}_encoder.joblib')
y_encoder = joblib.load('model/y_encoder.joblib')

scalers = {}
for feature in X[6:]:
  scalers[f'{feature}_scaler'] = joblib.load(f'model/{feature}_scaler.joblib')

pca = joblib.load("model/pca.joblib")
model = joblib.load("model/model.joblib")

def data_preprocessing(data):
  '''
  Input and output in dataframe form 
  '''
  data = data.copy()
  df = pd.DataFrame()

  for feature in X[:6]:
    df[feature] = encoders[f'{feature}_encoder'].transform(data[feature])
  
  # PCA
  for feature in X[6:]:
    if feature == 'Scholarship_holder':
      df[feature] = scalers[f'{feature}_scaler'].transform(np.asarray(data[feature]).reshape(-1,1))[0]
    else:
      data[feature] = scalers[f'{feature}_scaler'].transform(np.asarray(data[feature]).reshape(-1,1))[0]

  data = data.copy().reset_index(drop=True)
  df[['pca_1', 'pca_2', 'pca_3']] = pca.transform(data[X[7:]])
  
  return df

st.title('Student Performance Prediction')
st.warning('''
         ###### ⚠️ Please input some information to predict the student performance
         ''')

Course = st.selectbox('Course', encoders['Course_encoder'].classes_, index=None, placeholder="Select Course...")
Curricular_units_1st_sem_approved = int(st.slider('Curricular Units 1st Semester Approved', 0, 26))
Curricular_units_1st_sem_grade = float(st.number_input('Curricular Units 1st Semester Grade', 0, 20))
Curricular_units_2nd_sem_approved = int(st.slider('Curricular Units 1st Semester Approved', 0, 20))
Curricular_units_2nd_sem_grade = float(st.number_input('Curricular Units 2nd Semester Grade', 0, 20))
Application_mode = st.selectbox('Application Mode', encoders['Application_mode_encoder'].classes_, index=None, placeholder="Select an Aplication Mode...")
Scholarship_holder = st.radio('Scholarship Holder', ['Yes', 'No'], index=1)
Tuition_fees_up_to_date = st.radio('Tuition Fees UpToDate', ['Yes', 'No'], index=0)
Mothers_qualification = st.selectbox('Mothers Qualification', encoders['Mothers_qualification_encoder'].classes_, index=None, placeholder="Select a Qualification of Mother...")
Fathers_qualification = st.selectbox('Fathers Qualification', encoders['Fathers_qualification_encoder'].classes_, index=None, placeholder="Select a Qualification Father...")
Mothers_occupation = st.selectbox('Mothers Occupation', encoders['Mothers_occupation_encoder'].classes_, index=None, placeholder="Select Mothers Occupation...")
Fathers_occupation = st.selectbox('Fathers Occupation', encoders['Fathers_occupation_encoder'].classes_, index=None, placeholder="Select Fathers Occupation...")

ok = st.button('**Predict**')
if ok:
  try:
    data = pd.DataFrame([[
      Application_mode, Course, Fathers_qualification, Mothers_qualification, Fathers_occupation, Mothers_occupation, Scholarship_holder,
      Tuition_fees_up_to_date, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade, Curricular_units_2nd_sem_approved,
      Curricular_units_2nd_sem_grade
      ]],
    columns=[
      'Application_mode', 'Course', 'Fathers_qualification', 'Mothers_qualification', 'Fathers_occupation', 'Mothers_occupation', 'Scholarship_holder',
      'Tuition_fees_up_to_date', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_approved',
      'Curricular_units_2nd_sem_grade'
      ])
    data = data.replace(
      {'Tuition_fees_up_to_date': {'Yes': 1, 'No': 0},
       'Scholarship_holder': {'Yes': 1, 'No': 0}
      })
    df = data_preprocessing(data)
    predicted = model.predict(df)
    result = y_encoder.inverse_transform(predicted)[0]
      
    if result == 'Graduate':
      result_text = """
      #### This Student is Predicted to :green-background[:green[{}]]
      """.format(result)
    else:
      result_text = """
      #### This Student is Predicted to :red-background[:red[{}]]
      """.format(result)

    def stream_data():
      for word in result_text.split(" "):
        yield word + " "
        time.sleep(0.1)

    st.write_stream(stream_data)
  except ValueError:
    st.error('Please Complete The Information Above:smiley:')
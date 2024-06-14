import streamlit as st
from st_pages import Page, show_pages

st.logo('logo.png')

show_pages([
     Page("app.py", "Home", "🏠"),
     Page("predict_page.py", "Predict", ":male-student:"),
     Page("explore_page.py", "Explore", "🔍")
    ])

st.image('image.png')

st.markdown('''
         This Web Application is designed to help predict students in completing their studies based on some inputted information related
         to each student's performance. This prediction is made using Machine Learning models that are trained and tested using data of
         students who have graduated and some who have dropped out with the *Gradient Boosting* algorithm.
         ''')
st.markdown('''
            ##### How to Use:
                
            1. Navigate tab on the symbol(>) located in the top-left corner of the screen.
            2. Click on the desired tab among 'Home', 'Predict', or 'Explore' to access the page.
            3. In order to make a prediction, click on the 'Predict' tab:
               - Enter the appropriate information in the input fields.
               - To see the prediction results based on the data you have entered, click on the 'Predict' button.
            ''')
st.markdown('''
            ##### Disclaimer:
                
            It should be noted that the accuracy of the predictions provided by this web application may not always be guaranteed. In the event of any doubt, it is recommended that the values be entered again and the prediction verified.
            ''')

st.subheader('\n')
st.subheader('\n')
st.subheader('\n')
st.subheader('\n')
st.subheader('\n')

st.page_link('https://github.com/MuhamadSyarifFakhrezi', label='Muhamad Syarif Fakhrezi:copyright:')

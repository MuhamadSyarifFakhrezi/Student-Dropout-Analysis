import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.logo('logo.png')

st.title('Explore Student Data')

explore_df = pd.read_csv('explore_df.csv')
enrolled_df = pd.read_csv('enrolled_df.csv')

tab1, tab2 = st.tabs(["Former Students", "Enrolled Students"])

with tab1:
    st.subheader('Data of Former Students')
    st.dataframe(explore_df)

    st.write(
        '''
    #### Percentage by Graduation Status
    '''
    )
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(explore_df.groupby('Status').Status.count(), labels=['Dropout', 'Graduate'], autopct='%.1f%%', colors=['#FFDE59', '#3E397A'])

    st.pyplot(fig)

    st.write(
        '''
    #### Count of Students by Course
    '''
    )
    fig, ax = plt.subplots()
    sns.countplot(data=explore_df, y='Course', hue='Status', palette=['#FFDE59', '#3E397A'])
    ax.set_xlabel(None)
    ax.set_ylabel(None)

    st.pyplot(fig)

with tab2:
    st.subheader('Data of Enrolled Students')
    st.write('The following represents enrolled student data predicted by the machine learning model used in this prediction system.')
    st.dataframe(enrolled_df)

    st.write(
        '''
    #### Percentage by Graduation Status
    '''
    )
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(enrolled_df.groupby('Status').Status.count(), labels=['Dropout', 'Graduates'], autopct='%.1f%%', colors=['#FFDE59', '#3E397A'])

    st.pyplot(fig)

    st.write(
        '''
    #### Count of Students by Course
    '''
    )
    fig, ax = plt.subplots()
    sns.countplot(data=enrolled_df, y='Course', hue='Status', palette=['#FFDE59', '#3E397A'])
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    
    st.pyplot(fig)

import streamlit as st 
import pandas as pd

# Text input from user and give output

st.title('User input app')

name=st.text_input('Enter your Name ')

if name:
    st.write('Your Name is :',name)

# Dropdown 

options=['CSE','ICE','EEE','CE','ME']
dept=st.selectbox('Choose Your Department: ',options)
st.write(f"Your Department is : {dept}")


# slider
age=st.slider('Choose Your Age:',0,100,25)
st.write('Your age is :',age)


# upload file
uploaded_file=st.file_uploader('Choose your file:',type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)


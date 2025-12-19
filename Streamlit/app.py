import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

import streamlit  as st 

# set a Title 
st.title("Our First Website")


# write Text

st.write('I am Developer')


# Creta a datafram and show
df=pd.DataFrame({
    'Name':['Masum','oishe','sabrina'],
    'Taka':[10,1000,2000]
})
st.write('This is our Dataframe')
st.write(df)

# creta a linerchart
chart_data=pd.DataFrame(np.random.randn(10,3),columns=['A','B','C'])
st.line_chart(chart_data)
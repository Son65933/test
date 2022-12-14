import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('Bastar Craton.csv')

df

df.loc[:,['Si', 'Mg', 'Ca']]

#x_data = 'Mg'
#y_data = 'Si'

#plt.show(x_data, y_data)
            
st.title('First app')

sell = st.selectbox('Selection', ['Si','Mg','Ca'])

st.write('Deine Auswahl ist: ', sell) 


fig, ax = plt.subplots()

ax.scatter(df[sell], df['Mg'])

plt.xlabel(sell)  
plt.ylabel(sell)


st.pyplot(fig)

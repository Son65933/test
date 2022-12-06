import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


pd.read_csv('Bastar Craton.csv')
            
st.title('First app')

sell = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl ist: ', sell)

x= np.linspace(0, 50, 50)

fig, ax = plt.subplots()

ax.plot(x, x**sell)


st.pyplot(fig)

import streamlit as st

#st.write('Hello World')

import matplotlib.pyplot as plt
import numpy as np

st.title('First app')

sell = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl ist: ', sell)

x= np.linspace(0, 50, 50)

fig, ax = plt.subplots()

ax.plot(x, x**sell)


st.pyplot(fig)

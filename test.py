import streamlist as st

#st.write('Hello World')

import matplotlib.pyplot as plt
import numpy as np

st.title('First app')

sell = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl ist: ', sell)

x= np.linespace(0, 50, 50)
plt.plot(x, x**2)


st.pyplot(fig)

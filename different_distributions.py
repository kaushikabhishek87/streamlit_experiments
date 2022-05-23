import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# st.header('Different type of Distributions')

# st.subheader('Normal distribution')
# fig = plt.figure(figsize=(10, 7))
# value = np.random.normal(loc=0.0, scale=1, size=1000)
# sns.distplot(value)
# st.write(fig)
#
# st.subheader('Uniform distribution')
# fig = plt.figure()
# value = np.random.uniform(low=0.0, high=1, size=1000 )
# sns.distplot(value)
# st.write(fig)

options = st.multiselect("Choose distributions", ['Normal', 'Uniform'], ['Normal'])

for i in options:
    if i == 'Normal':
        st.subheader('Normal distribution')
        fig = plt.figure()
        value = np.random.normal(loc=0.0, scale=1, size=1000)
        sns.distplot(value)
        st.write(fig)

    elif i == 'Uniform':
        st.subheader('Uniform distribution')
        fig_1 = plt.figure()
        value_1 = np.random.uniform(low=0, high=1, size=1000)
        sns.distplot(value_1)
        st.write(fig_1)
#
# plt.show()
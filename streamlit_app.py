import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib_inline
import config
from datetime import time, datetime
_=""" Day 2 """
# st.write("Hello World")

_="""Day 3"""

"""First app deploy"""

# st.magicEnabled = False
# st.header('st.button')
#
# if st.button('Say Hello'):
#     st.write(config.GREETING_MESSAGE)
# else:
#     st.write('Goodbye for now')

# # Exmaple 1
# st.header('st.write')
#
# # Example 2
# st.write('Hello, *World* :sunglasses:')
#
# # Example 3
# st.write(1234)
#
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second columns': [10, 20, 30, 40]
# })
#
# st.write(df)
#
# # Example 4
# st.write('Below is a dataframe:', df, 'Above is a dataframe.')
#
# # Example 5
# df2 = pd.DataFrame(
#     np.random.rand(200, 3),
#     columns=['a','b','c']
# )
#
# c = alt.Chart(df2).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b',  'c']
# )
#
# st.write(c)

# st.header('Day 8')
# st.header('st.slider')
#
# # Example 1
# st.subheader('Slider')
#
# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm", age, 'years old')
#
# # Example 2
# st.subheader('Range slider')
#
# values = st.slider(
#     'Select a range from values',
#     0.0, 100.0, (25.0, 75.0)
# )
# st.write('values', values)
#
# # Example 3
# st.subheader('Range time slider')
#
# appointment = st.slider(
#     'Schedule your appointment:',
#     value=(time(11, 30), time(12, 45))
# )
# st.write("You are scheduled for:", appointment)
#
# # Example 4
# st.subheader('Datetime slider')
#
# start_time = st.slider(
#     'When do you start?',
#     min_value=datetime(2022, 5, 1, 9, 20),
#     max_value=datetime(2022, 6, 30, 9, 20),
#     value=(datetime(2022, 5, 20, 9, 20), datetime(2022, 6, 20, 9, 20)),
#     format="MM/DD/YY - hh:mm")
#
# st.write("start time:", start_time)

################# Seaborn in streamlit
df = pd.DataFrame({'col_1': list(range(0, 10)), 'col_2': list(range(0, 10))})

st.subheader('This is dataframe')
st.write(df.head())
st.subheader('This is scatter plot')
fig = plt.figure()
sns.scatterplot(data=df, x='col_1', y='col_2')
plt.xlabel('X axis')
plt.ylabel('Y axis')
st.pyplot(fig)

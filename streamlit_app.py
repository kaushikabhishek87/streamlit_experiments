import streamlit as st
# import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import config
# from streamlit_pandas_profiling import st_profile_report
from scipy import stats

# import ssl;
# ssl._create_default_https_context = ssl._create_stdlib_context

import pandas_profiling
from datetime import time, datetime
_=""" Day 2 """
# st.write("Hello World")

_="""Day 3"""

_="""First app deploy"""

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

##################### Day 8
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
# df = pd.DataFrame({'col_1': list(range(0, 10)), 'col_2': list(range(0, 10))})
#
# st.subheader('This is dataframe')
# st.write(df.head())
# st.subheader('This is scatter plot')
# fig = plt.figure()
# sns.scatterplot(data=df, x='col_1', y='col_2')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# st.pyplot(fig)

################ Day 9
# st.header('Line Chart')
#
# chart_data = pd.DataFrame(np.random.rand(20, 3), columns=['col1', 'col2', 'col3'])
#
# st.line_chart(chart_data)

################ Day 10
# st.header('st.selectbox')
#
# option = st.selectbox(
#     'What is your favourite color?',
#     ('Blue', 'Red', 'Green'))
#
# st.write('Your favourite color is ', option)
#

################ Day 11
# st.header('st.multiselect')
# options = st.multiselect(
#     'What are your favourite colors?',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])
#
# st.write('You selected:', options)

############### Day 12
# st.header('st.checkbox')
#
# st.write('What would you like to order?')
#
# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')
#
# if icecream:
#     st.write('Great! here is some 🍦')
# if coffee:
#     st.write('Great! here is some ☕️')
# if cola:
#     st.write('Great! here is some 🥤')

################ Day 14

# st.header('Streamlit_pandas_profiling')
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# pr = df.profile_report()
# print(pr)
# st_profile_report(pr)

################# Monet Carlo Simulations
st.header('Monte Carlo Simulation of Profit')

st.subheader('Profit = Revenue - FC - VC')

st.write("""Monte Carlo simulation of Profit when mean & std of Revenue, Fixed Cost & Variable cost is known, 
    assuming they have normal distribution.""")



st.write("""User can choose respective mean & std values for features.
            Final Profit KPIs are generated after 500 simulations on selected values""")
# rv_mean = 194500
# fc_mean = 60000
# vc_mean = 4000
#
# rv_std = 15000
# fc_std = 4000
# vc_std = 40000

rv_mean = st.slider('Revenue Mean', min_value=100000, max_value=200000, value=194500)
rv_std = st.slider('Revenue STD', min_value=10000, max_value=20000, value=15000)

fc_mean = st.slider('Fixed Cost Mean', min_value=10000, max_value=100000, value=60000)
fc_std = st.slider('Fixed Cost STD', min_value=1000, max_value=8000, value=4000)

vc_mean = st.slider('Revenue Mean', min_value=10000, max_value=70000, value=40000)
vc_std = st.slider('Revenue STD', min_value=20000, max_value=60000, value=40000)

rv_col = stats.norm.rvs(rv_mean, rv_std, 500)
fc_col = stats.norm.rvs(fc_mean, fc_std, 500)
vc_col = stats.norm.rvs(vc_mean, vc_std, 500)

df = pd.DataFrame({'Revenue': rv_col,
                   'Fixed_Cost': fc_col,
                   'Variable_Cost': vc_col})

df['Profit'] = df['Revenue'] - df['Fixed_Cost'] - df['Variable_Cost']

fig = plt.figure(figsize=(10,5))
sns.lineplot(data=df)
st.pyplot(fig)

profit_mean = df['Profit'].mean()
profit_std = np.std(df[['Profit']].values)
profit_min = df['Profit'].min()
profit_max = df['Profit'].max()
risk_of_loss = (df[df['Profit'] < 0].shape[0])/500

st.write('Mean Profit:', profit_mean)
st.write('STD Profit:', profit_std)
st.write('Min Profit:', profit_min)
st.write('Max Profit:', profit_max)
st.write('Risk of loss:', risk_of_loss)




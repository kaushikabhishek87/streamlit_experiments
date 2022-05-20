import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import config
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

# Exmaple 1
st.header('st.write')

# Example 2
st.write('Hello, *World* :sunglasses:')

# Example 3
st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second columns': [10, 20, 30, 40]
})

st.write(df)

# Example 4
st.write('Below is a dataframe:', df, 'Above is a dataframe.')

# Example 5
df2 = pd.DataFrame(
    np.random.rand(200, 3),
    columns=['a','b','c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b',  'c']
)

st.write(c)


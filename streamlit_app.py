import streamlit as st
import config
_=""" Day 2 """
# st.write("Hello World")

_="""Day 3"""

"""First app deploy"""

st.magicEnabled = False
st.header('st.button')

if st.button('Say Hello'):
    st.write(config.GREETING_MESSAGE)
else:
    st.write('Goodbye for now')
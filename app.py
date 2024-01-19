import streamlit as st

st.title("Streamlit Template Application")

col1, col2 = st.columns(2)
with col1:
    button1 = st.button('Button 1')
with col2:
    button2 = st.button('Button 2')

if button1:
    st.write('Button 1 clicked!')
if button2:
    st.write('Button 2 clicked!')


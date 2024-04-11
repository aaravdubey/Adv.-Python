import streamlit as st
import pandas as pd

st.write("Section X Page")

# st.write(st.session_state.data)

d = pd.read_csv("C:/Users/daara/Downloads/Recruitment Form (Responses) - Form responses 1.csv")
st.write(d)
import streamlit as st
import pandas as pd

st.set_page_config(
        page_title="Learning Streamlit",
        page_icon="✨",
    )

st.write("# Learning Streamlit 💻")

uploaded_file = st.file_uploader("Select a .csv file")
data = pd.DataFrame()
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.session_state.data = data

# data = pd.read_csv("../archive/shopping_behavior_updated.csv")
st.text("")
st.subheader("Dataset Overview")
if not data.empty:
    st.write(data.head())
else:
    st.write("No dataset uploaded.")


# .venv\Scripts\Activate.ps1
# streamlit run x.py --server.runOnSave true

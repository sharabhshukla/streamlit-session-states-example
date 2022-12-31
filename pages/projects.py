import streamlit as st


st.title("project 1")
username = st.session_state["username"]
st.write('This page is viewed by', username)
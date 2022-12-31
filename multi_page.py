import streamlit as st

st.set_page_config(
    page_title="Multi page app",
    page_icon="👋"
)

st.title("Main Page")
st.sidebar.success("Select a page")


if 'username' in st.session_state:
    st.write('username ->', st.session_state['username'])
else:
    with st.form('main_input'):
        username = st.text_input('Enter the username')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state['username'] = username
            st.write("username added!!")
            st.experimental_rerun()

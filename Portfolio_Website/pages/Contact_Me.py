import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_input = st.text_input("E-mail")
    message = st.text_area("Message")
    button = st.form_submit_button("Submit")

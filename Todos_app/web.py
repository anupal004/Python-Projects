import streamlit as st
import todofunctions as func

tasks = func.get_tasks()

st.title("My Tasks")

for task in tasks:
    st.checkbox(task)

st.text_input(label="", placeholder="Add your task...")
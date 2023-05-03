import streamlit as st
import todofunctions as func

tasks = func.get_tasks()


def add_task():
    new_task = st.session_state["new_task"] + "\n"
    tasks.append(new_task)
    func.write_tasks(tasks)


st.title("My Tasks")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        func.write_tasks(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add your task...",
              on_change=add_task, key='new_task')

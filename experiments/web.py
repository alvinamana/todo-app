import streamlit as st
from functions import get_todos, write_todos


todos = get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity!")


incrementer = 1

for todo in todos:
    st.checkbox(todo, key=incrementer)
    incrementer = incrementer + 1

st.text_input(label="Enter a todo:", placeholder="Add new todo...")
import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]  # key of st.text_input
    todos.append(todo + '\n')
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)   # so that each todo would have unique key
    if checkbox:
        print(checkbox)
        print(index, todo)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  #to remove the selected item from session_state
        st.rerun()   #to halt and rerun the sript, so item is removed

st.text_input(label="Enter a todo: ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state  # this is to see what session state is


#to run the web-app, key in the following in the terminal
#      streamlit run web.py
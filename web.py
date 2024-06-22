import streamlit as st
import todofunc

todos = todofunc.get_todos()

# session_State is used to control the widgets in the application for that we have to provide the key it forms a dictionary type value
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todofunc.write_todos(todos)


st.title("My Todo-App")
st.subheader("This is my todo app")
st.write("This app increases the daily productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        todofunc.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


# st.text_input(label="Enter a new-todoe",)
st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

#  streamlit run web.py ---> to run code


#https://davidsiltroy-python-big-data-image-classification-main-op94jq.streamlit.app/
import streamlit as st
from streamlit_option_menu import option_menu




#1. as slidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title= "Team 1: JAD Solutions",
        options = ["Notebook", "IDE", "About us"]
    )

if selected == "Notebook":
    st.header('Thomas More - Big Data Team Assigment: Image Classification')

if selected == "IDE":
    st.write("Here is going to be an Epic/Awesome image classificatior program!")

if selected == "About us":
    body = st.container()
    body.write("Coming soon.... (in Winter)")


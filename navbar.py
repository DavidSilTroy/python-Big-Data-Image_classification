import streamlit as st
from streamlit_option_menu import option_menu
from showcase import *
from ide import *
from about_us import *

def navbar():
    #1. as slidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title= "Team 1: JAD Solutions",
            options = ["Showcase", "IDE", "About us"]
        )

    if selected == "Showcase":
        showcase()

    if selected == "IDE":
        ide()

    if selected == "About us":
        about_us()
        


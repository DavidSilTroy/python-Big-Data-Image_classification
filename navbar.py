import streamlit as st
from streamlit_option_menu import option_menu

from googledrive import *
from showcase import *
from eda import *
from about_us import *

def navbar():
    #1. as slidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title= "Team 1: JAD Solutions",
            options = ["Showcase", "EDA", "About us", "Google Drive"]
        )

    if selected == "Showcase":
        showcase()

    if selected == "EDA":
        eda()

    if selected == "About us":
        about_us()

    if selected == "Google Drive":
        googledrive()
        


import streamlit as st

url="https://streamlit.io/"

st.set_page_config(
    page_title='My Super App',
    page_icon=':ice_cream:',
)

st.title("Our Super Application")

st.markdown('# Our Better :red[Title]')

st.markdown('Welcome to our first [Streamlit](%s) project' % url)

st.select_slider(

    "Select your favourite color!",

    options = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],

    
)

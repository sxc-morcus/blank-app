import streamlit as st

url="https://streamlit.io/"

st.set_page_config(
    page_title='My Super App',
    page_icon=':ice_cream:',
)

st.title("Our Super Application")

st.markdown('# Our Better :red[Title]')

st.markdown('Welcome to our first [Streamlit](%s) project' % url)

color=st.select_slider(

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

st.markdown('My favourite color is :%s[▀]' % color)

user_input = st.text_input("Enter a custom message!", "_")

st.write('Customized Message:', user_input)

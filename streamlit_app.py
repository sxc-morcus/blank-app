import streamlit as st
import pandas as pd
from pathlib import Path

url="https://streamlit.io/"

st.set_page_config(
    page_title='My Super App',
    page_icon=':ice_cream:',
)


@st.cache_data
def import_csv():

    DATA_FILENAME = Path(__file__).parent/'data/data.csv'
    df = pd.read_csv(DATA_FILENAME)
    df = df[:1000]

    def income_to_midpoint(income_str):
        low, high = income_str.split('-')
        low = int(low[:-1])  # Remove 'k' and convert to int
        high = int(high[:-1])  # Remove 'k' and convert to int
        return (low + high) / 2  # Calculate midpoint


    df['Midpoint'] = df['Income'].apply(income_to_midpoint)
    grouped_data = df.groupby('Party')['Midpoint'].mean().reset_index()


    return sorted_df

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

df = import_csv()

st.dataframe(df)

st.line_chart(grouped_data.set_index('Party'))  


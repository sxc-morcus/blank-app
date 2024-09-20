import streamlit as st
import pandas as pd
from pathlib import Path

url="https://streamlit.io/"

dic = {"null": 0, "under $25,000": 1, "$25,001 - $50,000": 2, "$50,000 - $74,999": 3, "$75,000 - $100,000": 4, "$100,001 - $150,000": 5,"over $150,000": 6}
dic2 = {"Democrat": 0, "Republican": 1}

st.set_page_config(
    page_title='My Super App',
    page_icon=':ice_cream:',
)


@st.cache_data
def import_csv():

    DATA_FILENAME = Path(__file__).parent/'data/data.csv'
    df = pd.read_csv(DATA_FILENAME)
    df = df[:1000]

    df['Income'].replace(dic, inplace=True)
    df['Party'].replace(dic2, inplace=True)
    
    sorted_df= df.sort_values(by="Income")

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

st.line_chart(data=df, x= "Income", y= "Party")

st.write(df['Income'].value_counts())

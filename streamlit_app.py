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

    sorted_df= df.sort_values(by="Income")
    unique_income_intervals = sorted_df['Income'].unique().tolist()
    enconding_dict = {element: index for index, element in enumerate(unique_income_intervals)}
    sorted_df['Income'] = sorted_df['Income'].replace(enconding_dict)
    sorted_df['Income'] = sorted_df['Income'].astype(int)
    sorted_df= sorted_df.sort_values(by="Income")    
    

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


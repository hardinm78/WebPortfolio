import pandas
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Portfolio Website")
    content = """
    Hi, I'm a portfolio website developed by <NAME>.   
    """
    st.info(content)

content2 = "Below you can find apps ive made."
st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.info(row['description'] + " " + f"[Source Code]({row['url']})")
        st.image(str("images/" + row['image']), use_column_width=True)

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.info(row['description'] + " " + f"[Source Code]({row['url']})")
        st.image(str("images/" + row['image']), use_column_width=True)

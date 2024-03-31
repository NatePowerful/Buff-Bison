import streamlit as st

st.set_page_config(page_title="Buff Bison", page_icon="H")

st.title("chatwith websites")

with st.sidebar:
    st.header("settings")
    website_url = st.text_input("website URL")

st.chat_input("Type")
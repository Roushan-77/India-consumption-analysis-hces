import streamlit as st


def setup_page(title="Dashboard"):
    st.set_page_config(
        page_title=title,
        layout="wide",
        initial_sidebar_state="expanded"
    )
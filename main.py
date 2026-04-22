import streamlit as st
from dashboard.pages.dashboard_page import show_dashboard
from dashboard.pages.dataset_page import show_dataset
from dashboard.utils import setup_page

setup_page("Rural vs Urban Dashboard")
page = st.sidebar.selectbox("Navigation", ["Dashboard", "Dataset Viewer"])

if page == "Dashboard":
    show_dashboard()
else:
    show_dataset()
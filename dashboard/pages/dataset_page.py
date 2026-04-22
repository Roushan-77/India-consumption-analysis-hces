import streamlit as st
from dashboard.data_loader import load_all
from dashboard.components import dataset_selector


def show_dataset():
    st.title(" Dataset Viewer")

    data = load_all()

    option = dataset_selector()

    if option == "MPCE":
        df = data["mpce"]
    elif option == "Consumption Rural":
        df = data["consumption_rural"]
    elif option == "Consumption Urban":
        df = data["consumption_urban"]
    elif option == "Percent Rural":
        df = data["percent_rural"]
    else:
        df = data["percent_urban"]

    st.subheader("Preview")
    st.dataframe(df.head(20))

    st.subheader("Shape")
    st.write(df.shape)

    st.subheader("Columns")
    st.write(list(df.columns))
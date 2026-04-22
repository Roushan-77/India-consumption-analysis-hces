import streamlit as st


def show_kpis(state_data):
    col1, col2, col3 = st.columns(3)

    col1.metric("Rural MPCE", f"₹{state_data['rural'].values[0]:,.0f}")
    col2.metric("Urban MPCE", f"₹{state_data['urban'].values[0]:,.0f}")
    col3.metric("Gap", f"₹{state_data['gap'].values[0]:,.0f}")


def show_title():
    st.title("Rural vs Urban Consumption Dashboard")


def show_insights():
    st.subheader("Key Insights")

    st.write("""
    - Urban households consistently show higher expenditure than rural households  
    - Rural households spend a larger share on essential items like food  
    - Urban households spend more on services, education, and healthcare  
    - The consumption gap highlights economic disparity across regions  
    """)


def dataset_selector():
    return st.selectbox(
        "Select Dataset",
        ["MPCE", "Consumption Rural", "Consumption Urban", "Percent Rural", "Percent Urban"]
    )
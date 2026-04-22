import streamlit as st
from dashboard.data_loader import load_all
from dashboard.preprocessing import preprocess_all
from dashboard.components import show_kpis, show_title, show_insights
from dashboard.charts import (
    plot_top_gap,
    plot_state_comparison,
    plot_spending_bar,
    plot_pie,
    plot_percentage_bar
)


def show_dashboard():
    show_title()

    data = load_all()
    clean = preprocess_all(data)

    df_mpce = clean["mpce"]
    df_rural = clean["consumption_rural"]
    df_urban = clean["consumption_urban"]
    df_pct_rural = clean["percent_rural"]
    df_pct_urban = clean["percent_urban"]

    st.sidebar.header("Controls")

    state = st.sidebar.selectbox("Select State", df_mpce["state"].unique())

    chart_type = st.sidebar.selectbox(
        "Select Analysis",
        ["Income Gap", "Spending (₹)", "Spending (%)"]
    )

    state_data = df_mpce[df_mpce["state"] == state]

    show_kpis(state_data)

    col1, col2 = st.columns([2, 1])

    if chart_type == "Income Gap":
        with col1:
            fig = plot_state_comparison(state_data)
            st.pyplot(fig)

        with col2:
            fig2 = plot_top_gap(df_mpce)
            st.pyplot(fig2)

    elif chart_type == "Spending (₹)":
        rural_row = df_rural[df_rural["state"] == state]
        urban_row = df_urban[df_urban["state"] == state]

        with col1:
            fig = plot_spending_bar(rural_row, urban_row)
            st.pyplot(fig)

        with col2:
            fig2 = plot_pie(
                rural_row["food_total"].values[0],
                rural_row["nonfood_total"].values[0],
                "Rural Distribution"
            )
            st.pyplot(fig2)

    elif chart_type == "Spending (%)":
        rural_row = df_pct_rural[df_pct_rural["state"] == state]
        urban_row = df_pct_urban[df_pct_urban["state"] == state]

        with col1:
            fig = plot_percentage_bar(rural_row, urban_row)
            st.pyplot(fig)

        with col2:
            fig2 = plot_pie(
                rural_row["food_percent"].values[0],
                rural_row["nonfood_percent"].values[0],
                "Rural % Distribution"
            )
            st.pyplot(fig2)

    show_insights()
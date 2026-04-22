#  Rural vs Urban Consumption Analysis (HCES 2023–24)

**Live Demo:**: [Click here -> Dashboard](https://india-consumption-analysis-hces-v4v6dvbgcpjfutlmta9fbt.streamlit.app/)

---

##  Overview

This project analyzes **rural vs urban consumption patterns in India** using data from the **Household Consumption Expenditure Survey (HCES) 2023–24)**.

The goal is to understand:
* Economic differences between rural and urban households
* Spending behavior across categories (food, education, healthcare, services)
* How expenditure distribution reflects development and living standards
An interactive **Streamlit dashboard** is built to visualize insights in a clear and user-friendly way.

---

## Dataset Source

* Official HCES dataset (MoSPI):
  [esankhyiki](https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?page=0&search=&product=HCES)

* Dataset used in this project (GitHub):
  [click here](https://github.com/Roushan-77/India-consumption-analysis-hces/tree/main/dataset)

###  Dataset Used
* **Statement 1 (MPCE):** Rural vs Urban expenditure comparison
* **Statement 3R & 3U:** Category-wise spending in ₹ (food, education, health, services)
* **Statement 4R & 4U:** Percentage distribution of expenditure across categories
These datasets together provide a complete view of **how much people spend, where they spend, and spending priorities**.
---

## Features

* Rural vs Urban MPCE comparison
* Spending analysis (₹ values)
* Percentage-based expenditure insights
* Key insights on economic disparity
* Dataset viewer for exploration

---

## Key Insights

* Urban households consistently spend more than rural households
* Rural spending is focused on **essential consumption (food)**
* Urban households spend more on **education, healthcare, and services**
* A shift from food → non-food expenditure indicates **higher development levels**
* Significant variation exists across states

---

## Tech Stack

* Python
* Pandas
* Matplotlib
* Streamlit
* Jupyter Notebook

---

## Run Locally

```bash
git clone https://github.com/Roushan-77/India-consumption-analysis-hces.git
cd India-consumption-analysis-hces

pip install -r requirements.txt
streamlit run main.py
```
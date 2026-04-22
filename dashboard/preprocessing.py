import pandas as pd

def clean_mpce(df):
    df = df.copy()

    df = df.rename(columns={
        'State/UT': 'state',
        'Average MPCE - Rural': 'rural',
        'Average MPCE - Urban': 'urban'
    })

    df['rural'] = df['rural'].astype(str).str.replace(',', '').astype(float)
    df['urban'] = df['urban'].astype(str).str.replace(',', '').astype(float)
    df['gap'] = df['urban'] - df['rural']

    return df


def clean_consumption(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    if 'state/ut' in df.columns:
        df = df.rename(columns={'state/ut': 'state'})
    important_cols = [
        'state',
        'food_total',
        'nonfood_total',
        'education',
        'medical_hosp',
        'medical_non',
        'conveyance',
        'services'
    ]

    df = df[important_cols]
    df['health_total'] = df['medical_hosp'] + df['medical_non']
    return df

def clean_percentage(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    if 'state/ut' in df.columns:
        df = df.rename(columns={'state/ut': 'state'})
    df = df.rename(columns={
        'food: total (1-14)': 'food_percent',
        'non-food: total (16-30)': 'nonfood_percent',
        'education': 'education_percent',
        'medical (hospitalization)': 'medical_hosp_percent',
        'medical (non- hospitalization)': 'medical_non_percent',
        'conveyance': 'conveyance_percent',
        'consumer services excluding conveyance&': 'services_percent'
    })

    df['health_percent'] = (
        df['medical_hosp_percent'] + df['medical_non_percent']
    )

    return df

def preprocess_all(data_dict):
    df_mpce = clean_mpce(data_dict["mpce"])

    df_rural = clean_consumption(data_dict["consumption_rural"])
    df_urban = clean_consumption(data_dict["consumption_urban"])

    df_pct_rural = clean_percentage(data_dict["percent_rural"])
    df_pct_urban = clean_percentage(data_dict["percent_urban"])

    return {
        "mpce": df_mpce,
        "consumption_rural": df_rural,
        "consumption_urban": df_urban,
        "percent_rural": df_pct_rural,
        "percent_urban": df_pct_urban
    }
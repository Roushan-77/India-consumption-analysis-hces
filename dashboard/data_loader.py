import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dataset"

def load_mpce():
    file_path = DATA_DIR / "1.csv"
    df = pd.read_csv(file_path)
    return df

def load_consumption():
    df_3r = pd.read_csv(DATA_DIR / "3R.csv")
    df_3u = pd.read_csv(DATA_DIR / "3U.csv")
    return df_3r, df_3u

def load_percentage():
    df_4r = pd.read_csv(DATA_DIR / "4r.csv")
    df_4u = pd.read_csv(DATA_DIR / "4u.csv")
    return df_4r, df_4u

def load_all():
    df_mpce = load_mpce()
    df_3r, df_3u = load_consumption()
    df_4r, df_4u = load_percentage()
    return {
        "mpce": df_mpce,
        "consumption_rural": df_3r,
        "consumption_urban": df_3u,
        "percent_rural": df_4r,
        "percent_urban": df_4u}
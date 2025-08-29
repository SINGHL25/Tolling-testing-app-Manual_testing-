import pandas as pd

def load_testcases(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def save_testcases(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)


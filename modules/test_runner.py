
import pandas as pd

def update_status(df: pd.DataFrame, case_id: str, status: str, comments: str = ""):
    df.loc[df["ID"] == case_id, ["Status", "Comments"]] = [status, comments]
    return df

def get_suite_cases(df: pd.DataFrame, suite: str):
    return df[df["Suite"] == suite]

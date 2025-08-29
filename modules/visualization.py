
import plotly.express as px

def plot_status_distribution(df):
    return px.pie(df, names="Status", title="Test Case Status Distribution")

def plot_suite_progress(df):
    return px.histogram(df, x="Suite", color="Status", barmode="group", title="Suite Progress")

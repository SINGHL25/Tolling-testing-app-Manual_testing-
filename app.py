import streamlit as st
import pandas as pd
from modules.data_loader import load_testcases, save_testcases
from modules.test_runner import update_status, get_suite_cases
from modules.visualization import plot_status_distribution, plot_suite_progress
from modules.report_generator import export_pdf

st.set_page_config(page_title="MLFF Tolling SAT Test Manager", layout="wide")

st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["Upload Data", "Test Execution", "Dashboard", "Report"])

if "df" not in st.session_state:
    st.session_state.df = load_testcases("data/sample_testcases.csv")

df = st.session_state.df

if page == "Upload Data":
    st.title("📂 Upload Test Cases")
    file = st.file_uploader("Upload CSV", type="csv")
    if file:
        st.session_state.df = pd.read_csv(file)
        st.success("Test cases uploaded!")

elif page == "Test Execution":
    st.title("🧾 Test Execution")
    suite = st.selectbox("Select Test Suite", df["Suite"].unique())
    cases = get_suite_cases(df, suite)
    case_id = st.selectbox("Choose Test Case", cases["ID"])
    case = cases[cases["ID"] == case_id].iloc[0]
    st.write("**Title:**", case["Title"])
    st.write("**Description:**", case["Description"])
    st.write("**Expected Result:**", case["ExpectedResult"])
    status = st.radio("Update Status", ["Pending", "Pass", "Fail"])
    comments = st.text_area("Comments")
    if st.button("Save Result"):
        st.session_state.df = update_status(df, case_id, status, comments)
        save_testcases(st.session_state.df, "data/sample_testcases.csv")
        st.success("Result saved!")

elif page == "Dashboard":
    st.title("📊 Dashboard")
    st.plotly_chart(plot_status_distribution(df))
    st.plotly_chart(plot_suite_progress(df))

elif page == "Report":
    st.title("📑 Generate Report")
    if st.button("Export PDF"):
        export_pdf(df, "data/SAT_Test_Report.pdf")
        st.success("Report exported! (check data folder)")


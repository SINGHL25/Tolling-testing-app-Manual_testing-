import streamlit as st
import pandas as pd

# Define the expected headers
EXPECTED_HEADERS = [f"AT_RSS_{i}-{j}" for i in range(31, 56) for j in range(1, 11)]

st.title("📊 Test Case Analyzer")

uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Find missing columns
    missing_cols = [col for col in EXPECTED_HEADERS if col not in df.columns]

    # Auto-add missing columns with default values
    for col in missing_cols:
        df[col] = "N/A"   # could also use 0 or "MISSING"

    st.success(f"✅ CSV loaded with {len(missing_cols)} auto-added columns")

    # Show first 10 rows
    st.dataframe(df.head(10))

    # Allow download of cleaned file
    st.download_button(
        "Download Cleaned CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name="cleaned_testcases.csv",
        mime="text/csv",
    )


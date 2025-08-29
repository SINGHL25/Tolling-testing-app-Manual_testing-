# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Test Case Dashboard", layout="wide")

st.title("📊 Test Case Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file with test results", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Auto-handle missing columns (fill with "Not Available")
    required_columns = ["TestCaseID", "Description", "Result", "Comments"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = "Not Available"

    st.sidebar.header("🔍 Filters")
    # Filter by Result
    result_filter = st.sidebar.multiselect(
        "Filter by Result",
        options=df["Result"].unique(),
        default=df["Result"].unique()
    )
    # Keyword search
    keyword = st.sidebar.text_input("Search in Description")

    # Apply filters
    filtered_df = df[df["Result"].isin(result_filter)]
    if keyword:
        filtered_df = filtered_df[filtered_df["Description"].str.contains(keyword, case=False, na=False)]

    st.subheader("📋 Filtered Test Cases")
    st.dataframe(filtered_df)

    # Add comment option
    st.subheader("📝 Add a Comment")
    new_comment = st.text_area("Write your comment:")
    if st.button("Save Comment"):
        st.success("✅ Comment saved (demo mode, not persistent)")

    # Summary counts
    st.subheader("📌 Summary Statistics")
    summary = df["Result"].value_counts()
    st.write(summary)

    # Graphical representation
    st.subheader("📈 Result Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    summary.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
    ax.set_ylabel("Count")
    ax.set_title("Test Case Results")
    st.pyplot(fig)

    # Pie chart
    st.subheader("🥧 Pie Chart of Results")
    fig2, ax2 = plt.subplots()
    summary.plot(kind="pie", autopct='%1.1f%%', ax=ax2, startangle=90, colormap="Set3")
    ax2.set_ylabel("")
    st.pyplot(fig2)

    # Export option
    st.subheader("📤 Export Filtered Data")
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Filtered CSV", csv, "filtered_testcases.csv", "text/csv")

else:
    st.info("Please upload a CSV file to start.")




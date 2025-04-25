import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.set_page_config(page_title="MA-BI Team Chatbot", layout="centered")
st.image("https://cdn.pixabay.com/photo/2016/12/13/21/20/alien-1905155_640.png", width=80)
st.markdown("### MA-BI Team Chatbot")

# ✅ Replace this with your actual raw GitHub Excel file URL
GITHUB_RAW_URL = "https://github.com/Mariappsetl/etl_chatbot/commit/4335cf66ea9479fef5f95aa99e283a730ba8f835"

@st.cache_data
def load_pipeline_data():
    response = requests.get(GITHUB_RAW_URL)
    if response.status_code == 200:
        excel_data = BytesIO(response.content)
        df = pd.read_excel(excel_data)
        df.columns = df.columns.str.strip()
        df['Table Name'] = df['Table Name'].str.strip().str.lower()
        df['Pipeline Name'] = df['Pipeline Name'].fillna(method='ffill')
        return df
    else:
        st.error("Failed to load Excel file from GitHub.")
        return pd.DataFrame()

df_pipeline = load_pipeline_data()

user_input = st.text_input("Ask me about CMA or BSM (type 'exit' to quit):")

if user_input:
    st.write(f"You: {user_input}")
    lower_input = user_input.lower().strip()

    if lower_input.startswith("table:"):
        table_name = lower_input.split("table:")[1].strip()
        match = df_pipeline[df_pipeline["Table Name"] == table_name]
        if not match.empty:
            pipelines = match["Pipeline Name"].unique()
            st.success(f"Pipeline(s) for table `{table_name}`: {', '.join(pipelines)}")
        else:
            st.warning(f"No pipeline found for table name: `{table_name}`")

    elif lower_input == "exit":
        st.success("Goodbye! 👋")
    elif lower_input == "hi":
        st.write("Hi, I'm MA-BI team chatbot Beta version. Ask me things related to BI team ETL projects: CMA or BSM")
    elif lower_input == "who are you":
        st.write("I'm the MA-BI Team chatbot, here to assist you with info related to our ETL projects in CMA and BSM.")
    elif lower_input == "who is your developer":
        st.write("I was developed by the MA-BI Team to make accessing ETL-related info easier and quicker!")
    elif lower_input == "help":
        st.write("Try asking me about CMA, BSM, subscription details, pipeline links, or say 'exit' to quit.")
    elif lower_input == "project owner":
        st.write("Project owners differ for CMA and BSM. Please specify which one you're asking about (CMA/BSM).")
    elif lower_input == "cma project owner":
        st.write("The project owner for CMA ETL projects is Mariapps.")
    elif lower_input == "bsm project owner":
        st.write("The project owner for BSM ETL projects is Mariapps.")
    elif lower_input == "etl tool used":
        st.write("We primarily use Azure Data Factory (ADF), Azure managed instance, and Azure storage in our ETL processes.")
    elif lower_input == "frequency of pipeline run":
        st.write("Most of our pipelines are scheduled to run daily, with critical ones running every 4 hours.")
    elif lower_input == "how to raise an issue":
        st.write("You can raise issues by dropping an email to etl-support@mariapps.com or using our Jira service desk.")
    elif lower_input == "what is cma":
        st.write("CMA refers to our internal ETL project focused on consolidating data for reference.")
    elif lower_input == "what is bsm":
        st.write("BSM refers to our internal ETL project focusing on data integration and reporting.")
    elif "cma" in lower_input:
        st.write("What do you want to know in CMA?")
        if st.button("Subscription"):
            st.info("https://mariapps.sharepoint.com/:i:/s/bsm-bi/ES15Kg-qVkBKlazafQlA7ZEBgl7azTKMMTht3zny8BhM7A?e=p82fmY")
        if st.button("Pipeline Details"):
            st.info("CMA Link: https://mariapps.sharepoint.com/...")
    elif "bsm" in lower_input:
        st.write("What do you want to know in BSM?")
        if st.button("Subscription"):
            st.info("https://mariapps.sharepoint.com/:i:/s/bsm-bi/ER-qv25h-vhIvxw4_jVnqcoBYunBMV_Ntdhe_VvajA9DpA?e=w8eggm")
        if st.button("Pipeline Details"):
            st.info("BSM Link: https://mariapps.sharepoint.com/...")
    else:
        st.warning("Sorry I didn't get that. Try 'table: <table_name>' or keywords like 'cma', 'bsm', 'exit'.")

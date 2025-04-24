import streamlit as st

st.set_page_config(page_title="MA-BI Team Chatbot", layout="centered")

st.image("https://cdn.pixabay.com/photo/2016/12/13/21/20/alien-1905155_640.png", width=80)
st.markdown("### MA-BI Team Chatbot")

user_input = st.text_input("Ask me about CMA or BSM (type 'exit' to quit):")

if user_input:
    st.write(f"You: {user_input}")
    lower_input = user_input.lower()

    if lower_input == "exit":
        st.success("Goodbye! 👋")
    elif lower_input == "hi":
        st.write("Hi, I'm MA-BI team chatbot Beta version ask me things related to BI team ETL projects CMA or BSM")
        st.session_state.input = ""
    elif lower_input == "who are you":
    st.write("I'm the MA-BI Team chatbot 🤖, here to assist you with info related to our ETL projects in CMA and BSM.")

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
    st.write("We primarily use Azure Data Factory (ADF) and Azure managed instance and Azure storage in our ETL processes.")

elif lower_input == "frequency of pipeline run":
    st.write("Most of our pipelines are scheduled to run daily, with critical ones running every 4 hours.")

elif lower_input == "how to raise an issue":
    st.write("You can raise issues by dropping an email to etl-support@mariapps.com or using our Jira service desk.")

elif lower_input == "what is cma":
    st.write("CMA refers to our internal ETL project focused on Consolidateding data for reference.")

elif lower_input == "what is bsm":
    st.write("BSM refers to our internal ETL project focused on Consolidateding data for reference., focusing on data integration and reporting.")

    elif "cma" in lower_input:
        st.write("What do you want to know in CMA?")
        if st.button("Subscription"):
            st.info("https://mariapps.sharepoint.com/:i:/s/bsm-bi/ES15Kg-qVkBKlazafQlA7ZEBgl7azTKMMTht3zny8BhM7A?e=p82fmY")
            st.session_state.input = ""
        if st.button("Pipeline Details"):
            st.info("CMA Link: https://mariapps.sharepoint.com/...")
    elif "bsm" in lower_input:
        st.write("What do you want to know in BSM?")
        if st.button("Subscription"):
            st.info("https://mariapps.sharepoint.com/:i:/s/bsm-bi/ER-qv25h-vhIvxw4_jVnqcoBYunBMV_Ntdhe_VvajA9DpA?e=w8eggm")
            st.session_state.input = ""
        if st.button("Pipeline Details"):
            st.info("BSM Link: https://mariapps.sharepoint.com/...")
    else:
        st.warning("Sorry I didn't get that. Try 'cma', 'bsm', or 'exit'. I'm created specifically for providing MA ETL details.")



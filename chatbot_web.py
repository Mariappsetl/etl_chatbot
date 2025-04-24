import streamlit as st

st.set_page_config(page_title="MA-BI Team Chatbot", layout="centered")

st.image("https://www.mariapps.com/wp-content/uploads/team_shankar.png", width=80)
st.markdown("### MA-BI Team Chatbot")

user_input = st.text_input("Ask me about CMA or BSM (type 'exit' to quit):")

if user_input:
    st.write(f"You: {user_input}")
    lower_input = user_input.lower()

    if lower_input == "exit":
        st.success("Goodbye! 👋")
    if lower_input =="Hi":
        st.write("Hi, I'm MA-BI team chatbot Beta version ask me things related to BI team ETL projects CMA or BSM")
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
        st.warning("I didn't get that. Try 'cma', 'bsm', or 'exit'")

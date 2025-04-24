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
        st.write("The project owner for CMA ETL

import streamlit as st

st.set_page_config(page_title="Minimal Chatbot", layout="centered")

st.title("🤖 Minimal Chatbot")

user_input = st.text_input("Ask me about CMA or BSM (type 'exit' to quit):")

if user_input:
    st.write(f"You: {user_input}")
    lower_input = user_input.lower()

    if lower_input == "exit":
        st.success("Goodbye! 👋")
    elif "cma" in lower_input:
        st.write("What do you want to know in CMA?")
        if st.button("Subscription"):
            st.info("Directory is MariApps Marine Solutions Pte Ltd\nResource Group is Hub-RG\nSubscription is CMA")
        if st.button("Pipeline Details"):
            st.info("CMA Link: https://mariapps.sharepoint.com/...")
    elif "bsm" in lower_input:
        st.write("What do you want to know in BSM?")
        if st.button("Subscription"):
            st.info("Directory is Schulte Group\nResource Group is Smartdata-Application-Prod-We-RG\nSubscription is Smartdata")
        if st.button("Pipeline Details"):
            st.info("BSM Link: https://mariapps.sharepoint.com/...")
    else:
        st.warning("I didn't get that. Try 'cma', 'bsm', or 'exit'")

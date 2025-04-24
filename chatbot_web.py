import streamlit as st

st.set_page_config(page_title="Minimal Chatbot", layout="centered")

st.image("https://www.bing.com/images/search?view=detailV2&ccid=JMzpYLKG&id=5D5EA2A21DDAA23319C65EDB756ED5F5EA41656B&thid=OIP.JMzpYLKGdw-1ErTG56FT4QAAAA&mediaurl=https%3a%2f%2fwww.mariapps.com%2fwp-content%2fuploads%2fRamesh-S-lyer.png&exph=398&expw=288&q=ramesh+iyer+mariapps&simid=608010346193319579&FORM=IRPRST&ck=0A63D5AEC2411782B72B82B13EBB08EA&selectedIndex=1&itb=0", width=80)
st.markdown("### Minimal Chatbot")

user_input = st.text_input("Ask me about CMA or BSM (type 'exit' to quit):")

if user_input:
    st.write(f"You: {user_input}")
    lower_input = user_input.lower()

    if lower_input == "exit":
        st.success("Goodbye! 👋")
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

import streamlit as st

st.set_page_config(page_title="Minimal Chatbot", layout="centered")

st.image("https://www.google.co.in/imgres?q=sankar%20mariapps&imgurl=https%3A%2F%2Fbl-i.thgim.com%2Fpublic%2Fnews%2Feksad3%2Farticle54387085.ece%2Falternates%2FLANDSCAPE_1200%2Fsankar-raghavanjpg&imgrefurl=https%3A%2F%2Fwww.thehindubusinessline.com%2Fnews%2Fmariapps-marine-solutions-singapore-opens-office-in-kochi%2Farticle33578244.ece&docid=bFkfsLBXFUvX9M&tbnid=QQT05Iku_D7B8M&vet=12ahUKEwi1pLWrv_CMAxWscmwGHeAhKScQM3oECGQQAA..i&w=1200&h=675&hcb=2&itg=1&ved=2ahUKEwi1pLWrv_CMAxWscmwGHeAhKScQM3oECGQQAA", width=80)
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

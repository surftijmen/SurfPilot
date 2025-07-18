import streamlit as st
import requests

st.set_page_config(page_title="SurfPilot.ai - Influencer Co-Pilot")
st.title("🌊 SurfPilot.ai - Influencer Co-Pilot")

msg = st.text_area("Paste a brand email or message:")

if st.button("Analyze Message"):
    with st.spinner("Thinking..."):
        response = requests.post("http://localhost:8000/analyze", json={"message": msg})
        data = response.json()

        st.subheader("Summary")
        st.write(data["summary"])

        st.subheader("Extracted Info")
        st.write(data["info"])

        st.subheader("Suggested Reply")
        st.write(data["reply"])

        if st.button("Generate Invoice"):
            invoice_response = requests.post("http://localhost:8000/generate-invoice", json={"message": msg})
            st.download_button("Download Invoice", invoice_response.json()["invoice"], file_name="invoice.pdf")

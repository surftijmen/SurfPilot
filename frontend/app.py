import streamlit as st
import requests
import json

# Load profiles from private JSON
with open("data/profiles.json") as f:
    profiles = json.load(f)

st.set_page_config(page_title="SurfPilot.ai - Influencer Co-Pilot")
st.title("🌊 SurfPilot.ai - Influencer Co-Pilot")

msg = st.text_area("Paste a brand email or message:")

with st.sidebar:
    st.header("Select Influencer")
    selected = st.selectbox("Influencer", list(profiles.keys()))
    profile = profiles[selected]

    st.subheader("Loaded Profile")
    st.text(f"{profile['name']} - {profile['email']}")
    st.text(f"Tone: {profile['preferred_tone']}")
    st.text(f"Deck Size: {profile['deck_size']}")
    st.text(f"Location: {profile['location']}")
    st.markdown(f"**Socials:**<br>" + "<br>".join([f"{k}: {v}" for k, v in profile["socials"].items()]), unsafe_allow_html=True)

# ... (rest of your Streamlit code unchanged)

if st.button("Analyze Message"):
    with st.spinner("Thinking..."):
        response = requests.post("http://localhost:8000/analyze", json={
            "message": msg,
            "profile": profile  # send the dict directly!
        })
        data = response.json()

        st.subheader("Summary")
        st.write(data["summary"])

        st.subheader("Extracted Info")
        st.write(data["info"])

        st.subheader("Suggested Reply")
        st.write(data["reply"])

        # if "music" in msg.lower():
        #     try:
        #         with open(profile["templates"]["music_collab"]) as f:
        #             st.download_button("Download Music Collab Template", f.read(), file_name="music_reply.txt")
        #     except FileNotFoundError:
        #         st.warning("Music template not found.")

        try:
            with open(profile["media_kit_path"], "rb") as mk:
                st.download_button("Download Media Kit", mk, file_name="Media_Kit.pdf")
        except FileNotFoundError:
            st.warning("Media kit not found.")

        if st.button("Generate Invoice"):
            invoice_response = requests.post("http://localhost:8000/generate-invoice", json={"message": msg})
            st.download_button("Download Invoice", invoice_response.json()["invoice"], file_name="invoice.pdf")

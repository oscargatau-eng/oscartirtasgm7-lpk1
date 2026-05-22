import streamlit as st

st.title("🎈 oscar")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

action = st.menu_button("Export", options=["CSV", "JSON", "PDF"])
if action == "CSV":
    st.write("Exporting as CSV...")
elif action == "JSON":
    st.write("Exporting as JSON...")
elif action == "PDF":
    st.write("Exporting as PDF...")

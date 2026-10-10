import streamlit as st

st.set_page_config(page_title="World Cities", page_icon="🌍")

st.title("World Cities")
st.markdown("## Welcome")
st.write(
    "Welcome to the World Cities Streamlit app. This is the home page. "
    "Click the button below to open the main app."
)

st.write("---")

if st.button("Go to App"):
    st.switch_page("pages/app.py")

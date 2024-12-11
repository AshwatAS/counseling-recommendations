import streamlit as st

st.title('Hello! Welcome to career compass')
st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

# Collect the name here

# Start with data collection
st.subheader("Try and answer as accurately as possible! Don't worry these questions are helping you, not deciding your future.")
preferred_environment=st.selectbox("Preferred Work environment",("Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"))

import streamlit as st
from send_email import send_email


with st.form(key="email_form"):
    sender_email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",
                         ("Job Inquires", "Project Proposals", "Other"))
    text = st.text_area("Text")
    button = st.form_submit_button("Submit")
    if button:
        send_email(sender_email, topic, text)
        st.info("Your message was successfully sent")

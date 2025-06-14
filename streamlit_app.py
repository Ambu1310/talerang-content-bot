import streamlit as st
from post_generator import generate_post
from sheets_connector import save_to_sheet
import os

st.set_page_config(page_title="Talerang Content Bot", layout="centered")

st.title("📚 Talerang Social Media Post Generator")

week = st.date_input("Select Week Start Date")
audience = st.selectbox("Select Audience", [
    "School Students (13–17)",
    "College/Graduates (18–25)",
    "Corporate L&D/HR"
])
trend = st.text_input("Enter a Trending Topic in EdTech")

if st.button("Generate and Save Post"):
    with st.spinner("Generating..."):
        post = generate_post(trend, audience)
        save_to_sheet(week.strftime("%Y-%m-%d"), audience, trend, post)
        st.success("Post generated and saved successfully!")
        st.text_area("Generated Post", value=post, height=200)

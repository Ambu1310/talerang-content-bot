import streamlit as st
from post_generator import generate_post

st.set_page_config(page_title="Talerang Content Bot", layout="centered")

st.title("📚 Talerang EdTech Social Content Generator")
st.write("Generate LinkedIn-style posts based on trending EdTech topics.")

# Input form
with st.form("content_form"):
    trend = st.text_input("Enter the trending EdTech topic", placeholder="e.g., AI in personalized learning")
    audience = st.selectbox(
        "Select your target audience",
        ["School Students", "College Graduates", "Young Professionals", "Corporate Trainees"]
    )
    submitted = st.form_submit_button("Generate and Save Post")

# Handle form submission
if submitted:
    with st.spinner("Generating content..."):
        try:
            post = generate_post(trend, audience)
            st.success("✅ Post generated!")
            st.text_area("Generated Post", value=post, height=200)
        except Exception as e:
            st.error(f"❌ Failed to generate post: {e}")

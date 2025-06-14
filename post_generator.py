import streamlit as st
import openai

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_post(topic, audience):
    prompt = f"Generate a short, engaging LinkedIn post for the audience: {audience}. Topic: {topic}. Keep it educational, professional, and shareable."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"].strip()


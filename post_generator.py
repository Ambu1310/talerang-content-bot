import os
from openai import OpenAI

# Securely load your OpenAI key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_post(topic, audience):
    prompt = (
        f"Generate a short, engaging LinkedIn post for the audience: {audience}. "
        f"Topic: {topic}. Keep it educational, interesting, and aligned with EdTech trends."
    )
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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
"))

def generate_post(topic, audience):
    prompt = f"Generate a short, engaging LinkedIn post for the audience: {audience}. Topic: {topic}. Keep it educational and interesting."
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

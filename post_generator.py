import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(trend, audience):
    prompt = f"""
    Generate a highly engaging social media post idea for Talerang.
    Audience: {audience}
    Trend: {trend}
    Tone: positive, supportive, empowering, empathetic, clear, professional, progressive, welcoming
    Include emojis and hashtags.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

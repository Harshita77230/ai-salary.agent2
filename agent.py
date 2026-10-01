import os
from openai import OpenAI


def career_advice(salary, skills):

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return (
            "AI Career Advice is unavailable: the OPENROUTER_API_KEY "
            "environment variable is not set. Please add it in your Render "
            "dashboard under Environment → Secret Files / Environment Variables."
        )

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    prompt = f"""
    Salary: {salary}
    Skills: {skills}

    Give only:
    1. Short salary explanation
    2. 3 missing skills
    3. 5 step career roadmap

    Keep answer under 100 words.
    """

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

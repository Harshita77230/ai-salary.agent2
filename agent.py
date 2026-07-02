import ollama


def career_advice(salary, skills):

    prompt = f"""
    sSalary: {salary}
    Skills: {skills}

    Give only:
    1. Short salary explanation
    2. 3 missing skills
    3. 5 step career roadmap

    Keep answer under 100 words.
    """

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
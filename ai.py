from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api) 
model = "gpt-3.5-turbo-16k"


def chat_with_assistant(content):
    completion = client.chat.completions.create(
        model = model,
        messages=[
            {
                "role":"system", "content": "You are a human like assistant skilled in general task like alexa and google cloud. You dont have to reply in more than 20 words unless asks for. Act more like human, talk casually as you can."
            },
            {
                "role":"user",
                "content": content
            }
        ]
    )
    return completion.choices[0].message.content
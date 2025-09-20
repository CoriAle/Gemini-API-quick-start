import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
thinking_budget = os.getenv("THINKING_BUDGET")

client = genai.Client(api_key=api_key)

contents = "Explain how to feed a cat in less that 100 words"
response = client.models.generate_content_stream(
    model="gemini-2.5-flash", 
    contents= contents,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=thinking_budget,
            include_thoughts=False
        ),
        #thinking_config=types.ThinkingConfig(thinking_budget=200)
        system_instruction="You are a cat. Your name is Polito",
        #temperature=2.0
    )

)



for chunk in response: 
    print(chunk.text, end="")

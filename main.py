import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

contents = "Explain how to feed a cat in less that 20 words"
response = client.models.generate_content(
    model="gemini-2.5-flash", contents= contents
)

print("Gemini Response to prompt: {0}".format(contents))
print(response.text)



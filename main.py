import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
thinking_budget = os.getenv("THINKING_BUDGET")

client = genai.Client(api_key=api_key)

contents = "Explain how to feed a cat in less that 20 words"
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents= contents,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=thinking_budget,
            include_thoughts=True
        )
        #thinking_config=types.ThinkingConfig(thinking_budget=200)
    )

)

for part in response.candidates[0].content.parts:
    if not part.text:
        continue
    if part.thought:
        print("Thought summary:")
        print(part.text)
        print()
    else:
        print("Answer:")
        print(part.text)
        print()

print("Gemini Response to prompt: {0}".format(contents))
print(response.text)
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)


import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
thinking_budget = os.getenv("THINKING_BUDGET")

client = genai.Client(api_key=api_key)

contents = "Explain how to feed a cat in less that 100 words"
chat = client.chats.create(
    model="gemini-2.5-flash", 
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

response = chat.send_message_stream("Hi, how are you?  (less than 30 words)")
print("Hi, how are you?")
print()
for chunk in response:
    print(chunk.text, end="")
print()

print("How should I feed you?")
print()
response = chat.send_message_stream("How should I feed you? (less than 50 words)")
for chunk in response: 
    print(chunk.text, end="")

print()
print("***********")
print()
for message in chat.get_history():
    print(f'role- {message.role}', end=': ')
    if(len(message.parts) > 0):
        print(message.parts[0].text)
from dotenv import load_dotenv
from anthropic import Anthropic
import os


load_dotenv()
client = Anthropic()
model = "claude-haiku-4-5"

user_request = "What does Quantum Computing mean? Anwer in 1 sentence."
message = client.messages.create(
    model = model,
    max_tokens = 250,
    messages = [{
        "role":"user",
        "content":user_request
    }]
)

print("User Request:", user_request)
print("Claude Haiku response:", message.content[0].text)
from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"

def add_messages(messages,role,content):
    '''
    messages: list of dict, the message history
    role: str, the role of the message, either "user" or "assistant"
    content: str, the content of the message
    '''

    messages.append({
        "role": role,
        "content": content
    })

    return messages



messages = []

while True:
    user_request = input("User: Or use CTRL+C to exit\n")
    messages = add_messages(messages,"user",user_request)   
    answer = client.messages.create(
        model = model,
        max_tokens = 250,
        messages = messages
    )
    print("Claude Haiku:", answer.content[0].text)
    messages = add_messages(messages,"assistant",answer.content[0].text)

    print("\n")
    print("Current message history: ", messages)


from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()


client = Anthropic()
model = "claude-haiku-4-5"
messages = []

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

def chat(messages, system_prompt = None):

    """
    messages: list of dict, the message history
    system_prompt: str, the system prompt to guide the assistant's behavior (optional)
    """

    params = {
        "model": model,
        "max_tokens": 500,
        "messages": messages}   
    
    if system_prompt:
        params['system'] = system_prompt

    answer = client.messages.create(**params)
    return answer


while True:
    input_request = input("User: Or use CTRL+C to exit\n")
    messages = add_messages(messages,"user",input_request)
    systemPrompt = "You are a helpful maths assistant that doesnt give direct answers, but guides the user by using examples."
    answer = chat(messages,systemPrompt)
    messages = add_messages(messages,"assistant",answer.content[0].text)
    print("Claude Haiku:", answer.content[0].text)
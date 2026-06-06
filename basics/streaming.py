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

user_req = input("User: Or use CTRL+C to exit\n")
messages = add_messages(messages,"user",user_req)


################## Method 1 ###################

# stream = client.messages.create(
#     model = model,
#     max_tokens = 250,
#     messages = messages,
#     stream = True
# )

# for event in stream:
#     if event.type == 'content_block_delta':
#         print(event.delta.text,end="")

################### Method 2 ###################################
with client.messages.stream(
    model = model,
    max_tokens=500,
    messages=messages
) as stream:
    
    for text in stream.text_stream:
        print(text,end='')

#####################################



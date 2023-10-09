import openai
import chainlit as cl
import pickle
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

openai.api_key = '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'

model_name = "gpt-3.5-turbo"
settings = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

class Agent:
    "used to interact and record"
    def __init__(self, name, prompt, history_file=None):
        # Initialize the class
        self.name = name
        self.chat = ChatOpenAI(streaming=True, 
                               callbacks=[StreamingStdOutCallbackHandler()], 
                               temperature=1.0,
                               model="gpt-4",)

@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
async def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    msg = cl.Message(content="")

    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

def message(self, message):
    self.message_history.append(HumanMessage(content=message))
    resp = self.chat(self.message_history)
    print("\n")
    self.message_history.append(resp)
    self.save_conversation(f"{self.name}_conversation.json")
    message = "What is your character's name and what do they look like?"
    current_agent = player
    while True:
        print(f"{current_agent.name}:")
        resp = current_agent
        message = resp.chat
        if current_agent == player:
            current_agent = gm
        else:
            current_agent = player
    return resp



def save_conversation(self, filename):
    with open(filename, 'wb') as f:
        pickle.dump(self.message_history, f)

all_header = ''

with open("gm_header.txt") as f:
    gm_header = all_header + f.read()

gm = Agent("GM", gm_header)

with open("player_header.txt") as f:
    player_header = all_header + f.read()
player = Agent("Player", player_header)



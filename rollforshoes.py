from dotenv import load_dotenv

# Load environment variables
load_dotenv()

import pickle
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class Agent:
    def __init__(self, name, prompt, history_file=None):
        # Initialize the class
        self.name = name
        self.chat = ChatOpenAI(streaming=True, 
                               callbacks=[StreamingStdOutCallbackHandler()], 
                               temperature=1.0,
                               model="gpt-4",)
    
def message(self, message):
    self.message_history.append(HumanMessage(content=message))
    resp = self.chat(self.message_history)
    print("\n")
    self.message_history.append(resp)
    self.save_conversation(f"{self.name}_conversation.json")
    return resp
    
def save_conversation(self, filename):
    with open(filename, 'wb') as f:
        pickle.dump(self.message_history, f)

with open("gm_header.txt") as f:
    gm_header = f.read()

gm = Agent("GM", gm_header)

with open("player_header.txt") as f:
    player_header = f.read()
player = Agent("Player", player_header)

message = "What is your character's name and what do they look like?"
current_agent = player
while True:
    print(f"{current_agent.name}:")
    resp = current_agent.chat
    message = resp.chat
    if current_agent == player:
        current_agent = gm
    else:
        current_agent = player
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal, Annotated
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI,OpenAI
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage
from Features.Speech_to_text import speech_to_text
from Features.Text_to_speech import text_to_speech
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from langsmith import uuid7
from Features.call import make_call
from Features.open_app import open_app, close_app
from Gmail.manage_mail import manage_email
from dotenv import load_dotenv
import os
import sqlite3
import uuid
import time

load_dotenv()


def generate_thread_id():
    return uuid7()

CONFIG = {
    'configurable':{'thread_id':generate_thread_id()},
    'metadata': {'thread_id':generate_thread_id()},
    'run_name':'Voice_turn'
}

#print(text_to_speech(audio)) working good 
model = ChatOpenAI(model='gpt-4o-mini')
 
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]
    
search_tool = DuckDuckGoSearchRun()

tools = [search_tool, make_call, open_app, close_app, manage_email]
model_with_tools = model.bind_tools(tools)


def chat_node(state:ChatState):
    '''LLM node that may answer or request a tool'''
    message = state['messages']
    response = model_with_tools.invoke(message)
    return {'messages':response}


tool_node = ToolNode(tools)

connection  = sqlite3.connect(database='jarvis_DB', check_same_thread=False)

checkpointer = SqliteSaver(conn=connection)


graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)
graph.add_node('tools', tool_node)

graph.add_edge(START, 'chat_node')
graph.add_conditional_edges('chat_node', tools_condition)
graph.add_edge('tools', 'chat_node')

jarvis = graph.compile(checkpointer=checkpointer)

print("Jarvis is now listening... say 'stop' to exit.\n")

#print(text_to_speech(audio)) working good 

# out = jarvis.invoke({'messages':[HumanMessage(content='Hi jarvis open instagram and also manage my emails')]},config=CONFIG)

#out = jarvis.invoke({'messages':[HumanMessage(content=audio)]},config=CONFIG)

#print(text_to_speech(out['messages'][-1].content))

while True:
    #audio = speech_to_text()
    audio = input()
    time.sleep(0.5)
    if not audio:
        continue
    
    print(f"User: {audio}")
    
    if audio.lower() in ['exit', 'bye', 'quit', 'stop']:
        out = jarvis.invoke({'messages': [HumanMessage(content="Ok jarvis Thankyou for helping me")]},config=CONFIG)
        #text_to_speech(out['messages'][-1].content)
        print(out['messages'][-1].content)
        break
        
    try:
        result = jarvis.invoke(
            {'messages':[HumanMessage(content=audio)]},
            config=CONFIG
        )
        
        ai_msg  = result['messages'][-1].content
        print(f"Jarvis: {ai_msg}")
        #text_to_speech(ai_msg)
    except Exception as e:
        print(f"Error is: {e}")
        #text_to_speech("Sorry sir, Something went Wrong please wait")
        
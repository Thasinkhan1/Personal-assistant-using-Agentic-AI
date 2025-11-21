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
from dotenv import load_dotenv
import os
import sqlite3
import uuid


load_dotenv()
# audio = speech_to_text()

def generate_thread_id():
    thread_id = uuid7()
    return thread_id

CONFIG = {
    'configurable':{'thread_id':generate_thread_id()},
    'metadata': {'thread_id':generate_thread_id()},
    'run_name':'chat_turn'
}

#print(text_to_speech(audio)) working good 
model = ChatOpenAI(model='gpt-4o-mini')
 
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]
    
search_tool = DuckDuckGoSearchRun()

tools = [search_tool, make_call]
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

out = jarvis.invoke({'messages':[HumanMessage(content='Hlo how are you')]},config=CONFIG)

print(out['messages'][-1].content)
print(out)

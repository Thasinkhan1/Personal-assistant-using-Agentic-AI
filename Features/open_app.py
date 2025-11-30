from AppOpener import open, close
from langchain_core.tools import tool

@tool
def open_app(name:str):
    '''open a app that given you'''
    if name:
        open(name)
    else:
        print("Please give me the app name")

@tool       
def close_app(name:str):
    '''Close a app from the given name'''
    if name:
        close(name)
    else:
        return "There is no app open with the name of {name}"

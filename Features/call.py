from twilio.rest import Client
import os
from dotenv import load_dotenv
import json
from langchain_core.tools import tool

load_dotenv()

client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))



def get_contact_number(name:str):
    name = name.lower()
    
    with open('contact.json','r') as f:
        contacts = json.load(f)
        
    for contact, number in contacts.items():
        if name in contact.lower():
            return number
        
    return None 

@tool
def make_call(to_number:str):
    '''Make a call on the given contact name'''
    number = get_contact_number(to_number)
    if number is None:
        return f"Contact number not found for {to_number}"
    
    call = client.calls.create(
        to=number,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        url="http://demo.twilio.com/docs/voice.xml"
    )
    output = f"Calling {to_number}"
    return output

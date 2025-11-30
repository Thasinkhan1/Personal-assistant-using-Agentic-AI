from twilio.rest import Client
from dotenv import load_dotenv
import os
from call import get_contact_number
load_dotenv()
import pywhatkit

client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))



# def send_message(contact_name:str, message:str):
#     number = get_contact_number(contact_name)
#     if number is None:
#         return f"No contact Number found for {contact_name}"
#     msg = client.messages.create(
#         body=message,
#         from_="watsapp:+19106316451",
#         to=f"watsapp:{number}"      
#     )
    
#     return f"Watsapp message Sent. {msg.sid}"

def send_whatsapp(name: str, message: str):
    contact = get_contact_number(name)
    if not contact:
        return f"Contact '{name}' not found."

    #phone = contact["phone"]
    try:
        pywhatkit.sendwhatmsg_instantly(contact, message)
        return f"WhatsApp message sent to {name}"
    except Exception as e:
        return str(e)
    
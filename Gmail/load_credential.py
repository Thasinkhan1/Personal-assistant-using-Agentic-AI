import imaplib
import email
import os
import pandas as pd
from email.header import decode_header
import logging
import json
import yaml

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_credentials(filepath):
    """
    Load user credentials from a YAML file for email login.
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            credentials = yaml.load(content, Loader=yaml.FullLoader)
            user = credentials.get('user')
            password = credentials.get('password')
            
            if not user or not password:
                logging.error("User or password missing in the provided YAML file.")
                raise ValueError("Credentials not found or incomplete in yaml file.")
            return user, password
    except FileNotFoundError:
        logging.error("The specified YAML file was not found: {}".format(filepath))
        raise
    except yaml.YAMLError as e:
        logging.error("Error parsing YAML file: {}".format(e))
        raise
    
    
# Function to connect to Gmail's IMAP server
def connect_to_gmail_imap(user, password):
  
    imap_url = 'imap.gmail.com'
    try:
        my_mail = imaplib.IMAP4_SSL(imap_url)
        my_mail.login(user, password)
        my_mail.select('Inbox')
        logging.info("Connected to Gmail and selected Inbox successfully.")
        return my_mail
    except imaplib.IMAP4.error as e:
        logging.error("Error during IMAP login or Inbox selection: {}".format(e))
        raise
    except Exception as e:
        logging.error("Unexpected error: {}".format(e))
        raise
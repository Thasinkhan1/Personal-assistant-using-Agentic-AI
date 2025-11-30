import json
import pandas as pd
import logging
import imaplib

# Function to load a list of email addresses from a JSON file
def load_email_list(filepath):

    with open(filepath, 'r') as file:
        data = json.load(file)
        return data['emails']
    
    
# Function to identify and flag emails for deletion based on sender address
def get_emails_to_delete(mail, filepath):
    """
    Search and mark emails for deletion from specified senders.
    and return a DataFrame: A DataFrame containing email addresses and the count of emails marked for deletion.
    """
    list_of_emails = load_email_list(filepath)
    email_summary = pd.DataFrame(columns=['Email address', 'Number of email messages to be deleted'])

    for email_address in list_of_emails:
        try:
            status, messages = mail.search(None, f'FROM "{email_address}"')
            messages = messages[0].split()
            email_summary.loc[len(email_summary)] = [email_address, len(messages)]

            for msg_id in messages:
                mail.store(msg_id, "+FLAGS", "\\Deleted")
            logging.info(f"Marked {len(messages)} emails from {email_address} for deletion.")
        except imaplib.IMAP4.error as e:
            logging.error(f"Error processing emails from {email_address}: {e}")

    return email_summary
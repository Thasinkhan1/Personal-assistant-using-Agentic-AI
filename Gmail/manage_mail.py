from Gmail.load_credential import load_credentials, connect_to_gmail_imap
from Gmail.load_email_list import get_emails_to_delete
from langchain_core.tools import tool

@tool
def manage_email():
    '''Manage the Emails'''
    credentials_path = 'Gmail\gmail_access.yaml'
    try:
        # Attempt to load credentials from the specified YAML file.
        user, password = load_credentials(credentials_path)
    except Exception as e:

        print("Failed to load credentials: {}".format(e))
        return  

    
    try:
        mail = connect_to_gmail_imap(user, password)
    except Exception as e:
        
        print("Failed to connect to Gmail IMAP: {}".format(e))
        return  

    
    email_list_filepath = 'Gmail\email_list.json'
    
    try:
        # Load the list and mark emails from specified senders for deletion.
        summary = get_emails_to_delete(mail, email_list_filepath)
        print(summary) 
    except Exception as e:
        print("Failed to process emails: {}".format(e))

    finally:
        try:
            mail.expunge()  
            mail.close()   
            mail.logout()  
        except Exception as e:
            print("Failed during cleanup of IMAP session: {}".format(e))
import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

token = os.getenv("ACCESS_TOKEN")
version = os.getenv("VERSION")
number_id = os.getenv("PHONE_NUMBER_ID")
user = os.getenv("USER_NUMBER")

############# FOR SENDING MESSAGES MANUALLY #############
def send_txt_msg():
    url = f"https://graph.facebook.com/v22.0/{number_id}/messages"

    headers = {
        "Authorization" : f"Bearer {token}",
        "Content-type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": user,
        "type": "text",
    
        "text": {
            "body": "Hey i am sending this msg from vscode lol. " # use body to send msgs 
        }
    }
    
    response = requests.post(url=url, headers=headers, json=data)
    return response

re = send_txt_msg()
print(re.status_code)
print(re.json())

 
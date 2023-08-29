# Here we are going to use sandbox to send sms
# we are not using any senderID
 
import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

username = os.environ.get("username_sandbox")
api_key = os.environ.get("api_key_sandbox")

def send_sms(message: str, phone_number: str):
    
    headers = {
        "apikey": api_key,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    data = urlencode({
        "username": username,
        "to": phone_number,
        "message":message
    })

    url = "https://api.sandbox.africastalking.com/version1/messaging"

    try:
        response = requests.post(url=url, data=data, headers=headers)
        if response.status_code == 201:
            res = response.json()
            message_info = res["SMSMessageData"]["Message"]
            status = res["SMSMessageData"]["Recipients"][0]["status"]
            message_data = {"message_info": message_info, "status": status}
            print(message_data)
            
        
        else:
            print(f"Failed to send with status_code: {response.status_code}")
    
    except Exception as e:
        print(f"Opps Antony, an error occurred: {str(e)}")


def handle_send_function():
    message = "Hello there, is this africas talking?"
    phone_number = "+254712345678"    #set the phone number in international format
    send_sms(message=message, phone_number=phone_number)


if __name__ == "__main__":
    handle_send_function()
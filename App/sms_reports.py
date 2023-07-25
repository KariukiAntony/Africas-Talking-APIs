# Here we are going to use sandbox to send sms
# make sure you have a registered sender ID

from flask import Flask, request
 
import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

app = Flask(__name__)

username = os.environ.get("username_sandbox")
api_key = os.environ.get("api_key_sandbox")
short_code = os.environ.get("short_code")

def send_sms(message: str, phone_number: str, username: str, short_code: str):
    
    headers = {
        "apikey": api_key,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    data = urlencode({
        "username": username,
        "to": phone_number,
        "message":message,
        "from": short_code
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
    send_sms(message=message, phone_number=phone_number, username=username, short_code=short_code)


# here we will handle incoming messages from the phonenumber 

@app.post("/handle_incoming_messages")
def handle_incomimg_messages():
    incoming_message = request.values.get("text")
    sender = request.values.get("from")
    receiver = request.values.get("to")
    date = request.values.get("date")
    data = {"message": incoming_message, "sender": sender, "receiver": receiver, "date": date}
    print({"Incoming messages": data})

    return {"message": "message received successfully"}


''' here we will handle the derivery reports from the message we sent'''


@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
   id  = request.form["id"]
   status = request.values.get("status", None)
   phone_number = request.form["phoneNumber"]
   network_code = request.form["networkCode"]
   failure_reason = request.values.get("failureReason")

   data = {"id": id, "status": status, "phone_number": phone_number, "network_code": network_code, "failure_reason": failure_reason}
   print({"DELIVERY REPORTS": data})

   return {"message": "delivery reports"}


''' here we will handle the derivery reports from the message we sent '''

@app.route('/handle_bulk_sms_opt_out', methods=['POST'])
def handle_bulk_sms_opt_out():
    sender_id = request.values.get("senderId")
    phone_number = request.values.get("phoneNumber")
    data = {"sender_id": sender_id, "phonenumber": phone_number}
    print({"BULK_SMS_OPT-OUT": data})
    
    return {"message": "user opts out"}

    


if __name__ == "__main__":
    handle_send_function()
    app.run()
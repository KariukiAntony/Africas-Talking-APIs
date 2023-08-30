from flask import Blueprint, request

ussd = Blueprint("ussd", __name__)

response = ""
user_input = ""

@ussd.post("/handle_ussd")
def handle_ussd_app():
    global response
    global user_input
    session_id = request.values.get("sessionId")
    service_code = request.values.get("serviceCode")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text")
    user_input += text

    if text == "":
        response += "CON Choose what to check\n"
        response += "1. Relationship Status\n"
        response += "2. More Info\n"

    return  response
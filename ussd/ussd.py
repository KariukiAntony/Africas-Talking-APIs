from flask import Blueprint, request
from .love import get_relationship_status

ussd = Blueprint("ussd", __name__)

response = ""
user_input = ""  #storing all the user inputs
@ussd.post("/handle_ussd")
def handle_ussd_app():
    global response
    global user_input  #make it accessible in the function
    session_id = request.values.get("sessionId")
    service_code = request.values.get("serviceCode")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text")
    user_input = text.split("*")

    if text == "":
        response = "CON Choose what to check\n"
        response += "1. Relationship Status\n"
        response += "2. More Info\n"
    
    elif text == "1":
        response = "CON Enter boyfriend's name"

    elif len(user_input) == 2:  #check if user has already entered the boyfriend name
        response = "CON Enter girlfriend's name"
    
    elif len(user_input) == 3:
        male_name = user_input[1]
        female_name = user_input[2]
        result = get_relationship_status(male=male_name, female=female_name)
        response = f"END {result}"
    
    elif text == "2":
        response = " END This service is currently unavailabe"

    return  response
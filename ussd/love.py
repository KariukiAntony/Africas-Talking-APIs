import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key_Rapidapi")

def get_relationship_status(male: str, female: str):
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    params = {
        "sname": female,
        "fname": male
    }

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    try:
        res = requests.get(url=url, headers=headers, params=params)
        if res .status_code == 200:
            response = res.json()
            return {"Boyfriend": male, "Girlfriend": female, "Love Percentage": response["percentage"]+"%", "result": response["result'"]}
        
        else:
            print(f"Opps! antony, an error occured wiht status code: {res.status_code}")
    
    except Exception as e:
        print(f"Opps! antony, an error occured: {e}")

if __name__ == "__main__":
    get_relationship_status("Antony", "Ann")

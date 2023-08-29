from flask import Flask
import os

app = Flask(__name__)

@app.get("/home")
def home():
    return {"Message": "Hello world"}



if __name__ == "__main__":
    app.run(debug=True)
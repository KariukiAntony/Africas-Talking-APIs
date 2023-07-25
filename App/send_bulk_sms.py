""" Here we are going to send sms to a list of phone number usings the same criteria

    The only requirement we need is a list of phone numbers and the message.
 """

recepients = ["+254712345678", "+254712345677", "+254712345676", "+254712345675"]

message = "Hello there, this is africas talking sms api"

from send_sms_sandbox import send_sms


def handle_bulk_sms():
    for i in range(len(recepients)):
        send_sms(message, recepients[i])

if __name__ == "__main__":
    handle_bulk_sms()
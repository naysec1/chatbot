from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = 'ACede3d2748708cc27dfbac66513767642'
auth_token = '4d4fc399e4cc62e41afe60f5a8737d23'
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def process_message(body):
    message_body = request.form.get('Body')
    if 'name' not in message_body:
        response = MessagingResponse()
        response.message("Hi! What's your name?")
        return str(response)
    else:
        name = message_body.split('name ')[1]
        response = MessagingResponse()
        response.message(f"Hi, {name.capitalize()}! Nice to meet you.")
        return str(response)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)

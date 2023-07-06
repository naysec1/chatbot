from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def communicate():
	return "hello"

@app.route("/sms", methods=['POST'])
def sms_reply():
	#storing user input.
	msg=request.form.get('Body')
	
	#create reply
	resp = MessagingResponse()
	resp.message("you said")
	
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)

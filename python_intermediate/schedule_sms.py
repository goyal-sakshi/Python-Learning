#!/usr/bin/python
from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "ACd394c7c374a4f18be1bddbee4b4ddaa7"
# Your Auth Token from twilio.com/console
auth_token  = "9f43ebc37c0e325f649e9d42f356b289"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	to="+917009749029",         # twilio registered number
	from_="+15853041810",       # twilio number
        body="Hello from Python!")

print(message.sid)

from twilio.rest import TwilioRestClient

account_sid = "ACfc0a5a5d2c7827b9992cfb635c75067e" # Your Account SID from www.twilio.com/console
auth_token  = "b8d87fdca9b800d422fe0ba2891cd80a"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+13139718814",    # Replace with your phone number
    from_="+13133273089") # Replace with your Twilio number

print(message.sid)

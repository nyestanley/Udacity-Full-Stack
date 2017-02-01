from twilio.rest import TwilioRestClient

account_sid = "AC9feaea8acee6dc865ab147640e785f5e" # Your Account SID from www.twilio.com/console
auth_token  = "d763f4e42c3ae5082d153a9359088408"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+13139718814",    # Replace with your phone number
    from_="+13133273089") # Replace with your Twilio number

print(message.sid)

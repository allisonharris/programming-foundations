from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8ea88d699e248422e56084428cfa2a86"
# Your Auth Token from twilio.com/console
auth_token  = "06fede995c4266be23fb0da1d23721f2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+112242771663", 
    from_="+13143101576",
    body="Hey! This is Allison. I wrote python code to send this text. OMG!")

print(message.sid)


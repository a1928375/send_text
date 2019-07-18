from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1a09f2a9fbef1a07128da62ad9f8aebe"
# Your Auth Token from twilio.com/console
auth_token  = "b976faf02e557580295f2dabc8dc8a30"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886928899459", 
    from_="+12029198755",
    body="Hello from Python! My name is Arthur Shih!")

print(message.sid)

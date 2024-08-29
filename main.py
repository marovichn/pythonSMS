from twilio.rest import Client

account_sid = "ACCID"
auth_token = "TOKEN"
client = Client(account_sid, auth_token)

message = client.messages.create(from_='tw_number', to='input_number')

print(message.sid)
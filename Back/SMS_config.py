from twilio.rest import Client

account_sid = 'ACae6b3430341fde63009bb4ccb9881310'
auth_token = '0c517bd637320f5e88532f7ad523f3b9'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14783304454',  # user
    body='x',  # mensagem
    to='+5511994226153'  # cliente
)

print(message.sid)
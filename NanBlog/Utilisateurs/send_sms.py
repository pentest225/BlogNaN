from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC193493935fdba4e641054d7139783541'
auth_token = '050252cd07243b778449beb7ffaa038d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12026880556',
                     to='+22508432050'
                 )

print(message.sid)
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC87bcdc10483708c4d174405099e1bedd'
auth_token = '5b0fd2340344516a0f43bf8ca5deb864'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12057053851',
                     to='+22508432050'
                 )

print(message.sid)
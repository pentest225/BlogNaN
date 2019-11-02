# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='pharaone1er@gmail.com',
    to_emails='kanangamansedrickgael@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print((e.message))
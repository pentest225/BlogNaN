# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
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
    print(e.message)
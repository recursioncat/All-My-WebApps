from email.message import EmailMessage
import ssl
import smtplib
import os

def send_mail(email_reciever, subject, body):
    email_sender = 'alaaptuition@gmail.com'
    email_password = os.environ.get('Alaap Google Password')

    mail = EmailMessage()
    mail['From'] = email_sender
    mail['To'] = email_reciever
    mail['Subject'] = subject
    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, mail.as_string())


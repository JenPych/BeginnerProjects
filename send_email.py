from email.message import EmailMessage  # used to create/manipulate mail
import ssl  # used to secure connection between server and client
import smtplib  # used to send mails


email_sender: str = ""  # fill sender email
email_password: str = ""  # fill Password
email_receiver: str = ""  # fill receiver email

subject: str = "This is an email sent by using python"
body: str = ('''Greetings, User
This is an email sent to you using python. I am a beginner python programmer looking to learn AI.
Thank You''')

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())
    print("Success! E-mail sent.")

except Exception as e:
    print(f"Send e-mail failed. {e} ")


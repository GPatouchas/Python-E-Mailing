import smtplib


sender = input("Type your email: ")
receiver = input("Type the receivers email: ")
password = input("Type password: ")
subject = input("Type your subject: ")
body = input("Type your message: ")

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
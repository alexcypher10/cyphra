import os
import secrets
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def generate_verification_code():
    # sends a random 6 digit code for verification
    return str(secrets.randbelow(900000) + 100000)

def send_verification_email(to_email, code):
    # emails the user a verification mail
    sender = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("APP_PASSWORD")

    subject = "You cyphra Verification code"
    body = f"YOUR VERIFICATION CODE IS : {code}\n\nTHIS CODE EXPIRES IN 10 MINUTES "

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, to_email, msg.as_string())


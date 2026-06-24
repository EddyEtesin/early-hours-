import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email(name, recipient_email, html_content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Early Hours {__import__('datetime').datetime.now().strftime('%A, %B %d')}"
    msg["From"] = f"Early Hours <{SENDER_EMAIL}>"
    msg["To"] = recipient_email

    plain = f"Good morning {name}, your Early Hours brief is best viewed in an HTML-compatible email client."
    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        print(f"Sent to {name} at {recipient_email}")

    
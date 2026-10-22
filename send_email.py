import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(recipient, subject, body):
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise RuntimeError(
            "EMAIL_ADDRESS and EMAIL_PASSWORD must be set in the .env file."
        )

    message = MIMEMultipart()
    message["From"] = EMAIL_ADDRESS
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(
            EMAIL_ADDRESS,
            recipient,
            message.as_string(),
        )


if __name__ == "__main__":
    recipient = input("Enter the recipient email address: ").strip()

    send_email(
        recipient=recipient,
        subject="Test email from Python",
        body="Hello! This email was sent using Python and Gmail SMTP.",
    )

    print("Email sent successfully.")
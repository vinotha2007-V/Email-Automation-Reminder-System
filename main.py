import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_email(receiver, subject, body, attachment=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = receiver
    msg.set_content(body)

    # Attach file
    if attachment:
        with open(attachment, "rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print(f"Email sent to {receiver}")


if __name__ == "__main__":
    send_email(
        "receiver@gmail.com",
        "Test Email",
        "Hello from Python Automation!"
    )

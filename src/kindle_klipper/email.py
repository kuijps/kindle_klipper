import smtplib
from email.message import EmailMessage


def send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, email_content):
    msg = EmailMessage()
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(email_content)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)

import logging
import smtplib
from email.mime.text import MIMEText

logger = logging.getLogger()

GMAIL_USER = None
GMAIL_PASSWORD = None


def send_email(send_to: str, subject: str, body: str) -> bool:
    msg = MIMEText(body, 'plain', 'UTF-8')
    msg['From'] = f'"Friends Event Reminder" <{GMAIL_USER}>'
    msg['To'] = send_to
    msg['Reply-To'] = GMAIL_USER
    msg['Subject'] = subject
    msg.set_charset('UTF-8')

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, send_to, msg.as_string())
        server.close()
        return True

    except Exception as e:
        logger.exception("Something went wrong when sending email")
        return False

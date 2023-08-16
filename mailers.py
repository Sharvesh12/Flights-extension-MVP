import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from config import logging

logger = logging.getLogger(__name__)


class Mailer:
    """
    This class implements sending of emails.
    """
    email_sending = 'reporting3_bi_de@auto1.com'
    email_server_host = 'smtp.gmail.com'
    port = "587"

    def __init__(self, email_username, email_password):
        self.email_username = email_username
        self.email_password = email_password

    def send_email(self, subject: str, body: str, recipients: list,
                   # recipients_cc: list,
                   attachments: str = None):
        """
        Use this method to send an email. Bear in mind the size of the attachments
        shouldn't overpass the max email size for the mailing service.
        :param subject: Email subject
        :param body: Email body
        :param recipients: list of recipients
        :param attachments: list of paths to the attachments
        # :param recipients_cc: list of recipients in cc
        :return: None
        """
        logger.info(
            f"Sending email {subject} to {', '.join(recipients)}"
            f" with attachments: {attachments}"
        )

        msg = MIMEMultipart()
        msg['From'] = self.email_sending
        msg['To'] = ','.join(recipients)
        msg['Subject'] = subject
        # msg['CC'] = ','.join(recipients_cc)

        body = MIMEText(body)

        msg.attach(body)

        if attachments:
            # for attachment in attachments:
            attach_file = open(attachments, 'rb')
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload(attach_file.read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Disposition', 'attachment',
                               filename=attachments.split('/')[-1])
            msg.attach(payload)

        server = smtplib.SMTP(self.email_server_host, self.port)
        server.ehlo()
        server.starttls()
        server.login(self.email_username, self.email_password)
        server.sendmail(self.email_sending, recipients,
                        msg.as_string().encode('utf-8'))
        server.close()

        logger.info("Email sent successfully")


class SesMailer(Mailer):
    email_server_host = 'email-smtp.eu-west-1.amazonaws.com'

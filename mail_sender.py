import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

class MailSender:
    def __init__(self, email_sender, sender_passwd, email_recipient, email_cc, email_server, email_server_port):
        self.msg = MIMEMultipart()
        self.sender = email_sender
        self.passwd = sender_passwd
        self.recipient = email_recipient
        self.email_cc = email_cc
        self.email_server = email_server
        self.email_server_port = email_server_port
        self.subject = ""
        self.body = ""

    def context(self, subject, body):
        self.subject = subject
        self.body = body

    def attachment(self, exist_attachment, attachment_filepath):
        if exist_attachment:
            attachment = open(attachment_filepath,'rb')
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment", filename= os.path.basename(attachment_filepath))
            self.msg.attach(part)

    def write(self, exist_attachment, attachment_filepath):
        self.msg['From'] = self.sender
        self.msg['To'] = ",".join(self.recipient)
        self.msg['Cc'] = ",".join(self.email_cc)
        self.msg['Subject'] = self.subject

        self.msg.attach(MIMEText(self.body, 'plain'))
        self.attachment(exist_attachment, attachment_filepath)

    def send(self):
        recipients_list = self.recipient + self.email_cc
        server = smtplib.SMTP(self.email_server, self.email_server_port)
        server.ehlo()
        server.starttls()
        server.login(self.sender, self.passwd)
        server.sendmail(self.sender, recipients_list, self.msg.as_string())
        server.quit()

    def send_nologin(self):
        recipients_list = self.recipient + self.email_cc
        server = smtplib.SMTP(self.email_server, self.email_server_port)
        server.ehlo()
        server.sendmail(self.sender, recipients_list, self.msg.as_string())
        server.quit()

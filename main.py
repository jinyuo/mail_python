import time
import mail_sender


# ----- MAIN ------
# sender/recipient info
email_sender = 'exampleh@example.com'
sender_passwd = 'PASSWD'
email_recipient = ['exampleh@example.com']
email_cc = ['exampleh@example.com', 'exampleh@example.com']
email_server = 'smtp.gmail.com'
email_server_port = 587

# mail context
subject = time.strftime('%Y-%m-%d', time.localtime(time.time()))
body = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# attachment info
exist_attachment = True
attachment_filepath = 'FILE_PATH'

# init Mail essentail info
mail = mail_sender.MailSender(email_sender, sender_passwd, email_recipient, email_server, email_server_port)

# writing subject/body of mail
mail.context(subject, body)
mail.write(exist_attachment, attachment_filepath)

# sending mail
mail.send(login=False)

import smtplib, ssl


port = 465  # For SSL

smtp_server = "smtp.gmail.com"

#TODO set bot_email, bot_email_password, my_email

bot_email = "your_newly_created_bot@gmail.com"
bot_email_password = "your bot gmail account password"
my_email = "your_email@gmail.com"

# Create a secure SSL context
context = ssl.create_default_context()


SUBJECT = "Graphic Card Alert!!!"
TEXT = ""
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

def setMail(subject, text):
    new_message = 'Subject: {}\n\n{}'.format(subject, text)
    return new_message

def emailMySelf(new_subject, new_message):
    ready_mail = setMail(new_subject, new_message)
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(bot_email, bot_email_password)
        server.sendmail(bot_email, my_email, ready_mail)

def emailMySelf_Default():
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(bot_email, bot_email_password)
        server.sendmail(bot_email, my_email, message)

if __name__ == "__main__":
    emailMySelf("new graphic", "This is the body")

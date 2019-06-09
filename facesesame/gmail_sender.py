import gmail
import settings
from email.mime.image import MIMEImage


def sendImageByGmail(subject, body, image):

    if (settings.SEND_EMAIL is not True):
        return

    user = settings.GMAIL_USER
    password = settings.GMAIL_PASS
    client = gmail.GMail(user, password)
    to = settings.GMAIL_TO
    subject = "[facesesame] " + subject
    if image == '':
        message = gmail.Message(subject, to=to, text=body)
    else:
        attachment = MIMEImage(image, 'jpeg', filename="file.jpg")
        attachment.add_header('Content-Disposition',
                              "attachment; filename=file.jpg")

        message = gmail.Message(
            subject, to=to, text=body, attachments=[attachment])
    client.send(message)
    client.close()

# import smtplib
# from email.mime.text import MIMEText
# def send_mail(sender, recipients, body, subject, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ", ".join(recipients)
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#         smtp_server.login(sender, password)
#         smtp_server.sendmail(sender, recipients, msg.as_string())
#
#     print("Message sent!")
# # send_mail(sender, recipients, "{6:5, 3:3}", subject, password = password)
#
#
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_mail(sender, recipients, body, subject, password, attachment_path=None):
    # ایجاد پیام چند بخشی (متن + پیوست)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    # اضافه کردن بدنه ایمیل
    msg.attach(MIMEText(body, 'plain'))
    print("ydhufh7888888885874839789453")
    # اگر فایل پیوستی داریم، آن را اضافه می‌کنیم
    if attachment_path:
        with open(attachment_path, "rb") as f:
            file_attachment = MIMEApplication(f.read(), _subtype="txt")
            file_attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(file_attachment)

    # اتصال به سرور ایمیل و ارسال
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

    print("Message with attachment sent!")

# ارسال فایل متنی به عنوان پیوست
send_mail(
    sender=sender,
    recipients=recipients,
    body="This is the email body",
    subject=subject,
    password=password1_137979,
    attachment_path="document.txt"
)

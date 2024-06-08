import smtplib, ssl


def send_email(sender_email, topic, text):
    host = "smtp.gmail.com"
    port = 465
    username = "leobot1010@gmail.com"
    password = "vuihokpyyfphutnc"
    receiver = "leobot1010@gmail.com"
    context = ssl.create_default_context()

    message = f"""
From: {sender_email}
Topic: {topic}\n
{text}
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


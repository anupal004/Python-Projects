import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "anupaldeuri8@gmail.com"
password = "mzoqekmlyaqbfojn"

receiver = "deoriutjal@gmail.com"
context = ssl.create_default_context()

message = """ \
Subject: Greetings
Hello!! """
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


import smtplib
sender="anornymous99@gmail.com"
receiver=["anornymous99@gmail.com","duncansantiago18@gmail.com"]
message="""From: from person %s
To: to person %s
Content-Type:text/plain
Mime-version:1.0
Content-disposition: text
Subject:Mail testing
Just created this python script to send mails to any number of users and uploaded it to github.
"""%("anornymous99@gmail.com","anornymous99@gmail.com")
try:
    obj=smtplib.SMTP('smtp.gmail.com', 587)
    obj.starttls()
    obj.login("anornymous99@gmail.com","xcmbyzwvy")
    obj.sendmail(sender,receiver,message)
except Exception as error:
    print("Error: {}".format(error))
else:
    print("Message sent successfully to {}".format(receiver))
finally:
    print("Exiting the mail client program")

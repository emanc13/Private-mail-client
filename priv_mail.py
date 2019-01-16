import smtplib
from email.mime.text import MIMEText

def sendMail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print "Connecting..."
        smtpServer.ehlo() #identification
        print "Commencing encrypted session"
        smtpServer.starttls() #encrypt session
        smtpServer.login(user, pwd)
        print "Sending..."
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print "Success"
    except:
            print "Failed"
user = 'username'
pwd = 'password'
sendMail(user, pwd, 'target@tgt.tgt',\
    'Attn: Test', 'Hello World')             
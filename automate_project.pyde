import time
import datetime
while True:
  unix=int(time.time())
  time1=str(datetime.datetime.fromtimestamp(unix).strftime('%I:%M:%S:%p'))
  if time1=='11:36:00:AM':
    import smtplib
    gmailaddress = 'enter email address'
    gmailpassword = 'enter email app password'
    mailto = 'enter mail to address'
    SUBJECT='Tester'
    msg = 'this is a tester'
    message = 'Subject:Tester\n\nthis is a tester'.format(SUBJECT,msg)
    mailServer=smtplib.SMTP('smtp.gmail.com',587)
    mailServer.starttls()
    mailServer.login(gmailaddress,gmailpassword)
    mailServer.sendmail(gmailaddress, mailto, message)
    print('\n Sent!')
    mailServer.quit()
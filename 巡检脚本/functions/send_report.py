#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailto_list = ['admin@test.cc']
mail_host = "127.0.0.1"
mail_user = "user1"
mail_pass = "123"
mail_postfix = "test.cc"

def send_mail(to_list):

	msg = MIMEMultipart()
	
	msg['From'] = "admin"+"<"+mail_user+"@"+mail_postfix+">"
	msg['To'] = ";".join(to_list)
	msg['Subject'] = "Check Report"
	content = "Good Luck To You！"
	txt = MIMEText(content,'plain','gb2312')
	msg.attach(txt)
	
	att = MIMEText(open('./report.txt','rb').read(),'base64','gb2312')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment;filename=report.txt'
	msg.attach(att)
	try:
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user,mail_pass)
		server.sendmail(msg['From'],msg['To'],msg.as_string())
		server.close()
		return True
	except Exception,e:
		print str(e)
		return False

"""
if send_mail(mailto_list):
	print "发送成功"
else:
	print "发送失败"
"""

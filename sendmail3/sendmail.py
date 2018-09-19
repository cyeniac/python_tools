import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

#SMTP server
mail_host = ""
mail_username = ""
mail_password = ""

#发件人邮件地址
sender = ''
receivers = ['收件人邮件地址']
#邮件正文内容
content = "您好！这是一封测试邮件，请勿回复！给您带来的不便，敬请谅解！谢谢！^_^"

def sendEmail():
    #获取当前时间
    nowtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    message = MIMEText(content,'plain','utf-8')
    message['from'] = "{}".format(sender)
    message['to'] = ",".join(receivers)
    message['subject'] = "测试邮件" + nowtime

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(mail_username,mail_password)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("邮件成功发送")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    for i in range(2):#控制发送邮件个数
        time.sleep(2)
        sendEmail()

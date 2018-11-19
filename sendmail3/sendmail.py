import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#SMTP server
mail_host = "邮件服务器地址"
mail_username = "邮件账号"
mail_password = "邮件密码"

#发件人邮件地址
sender = '发件人邮箱'
receivers = ['收件人邮箱']

# 构造邮件
# nowtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
message = MIMEMultipart()
message['from'] = "{}".format(sender)
message['to'] = ",".join(receivers)
message['subject'] = "测试邮件"

#邮件正文内容
content = "您好！这是一封测试邮件，请勿回复！给您带来的不便，敬请谅解！谢谢！^_^"
message.attach(MIMEText(content, 'plain', 'utf-8'))

#邮件附件
attar_path = os.getcwd() + os.sep + 'attach'
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
                L.append(os.path.join(root, file))
    return L

for file in file_name(attar_path):
    filename = file.split(os.sep)[-1]
    #print(type(filename))
    att = MIMEText(open(file,'rb').read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s' % filename
    att.add_header('Content-Disposition','attachment',filename=('gbk','',filename))
    message.attach(att)




#发信
def sendEmail():
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(mail_username,mail_password)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("给{}发送邮件成功".format(receivers))
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    for i in range(1):#控制发送邮件个数
        sendEmail()
        time.sleep(5)

import imaplib
import email
from imapclient import imap_utf7
import time

class MyImap:
    def __init__(self,host,username,password):
        self.host = host
        self.username = username
        self.password = password


    #日志记录
    def logs(self,info):
        self.info = info
        Nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open("logs/myimaplogs.log","a",encoding='utf-8') as f:
            f.write(Nowtime + " :" + self.info + '\n')

    #用户登录
    def login(self):
        try:
            self.conn = imaplib.IMAP4_SSL(self.host)
            self.conn.login(self.username,self.password)
            info = 'User {0} login success'.format(self.username)
            self.logs(info)
        except self.conn.Error:
            info = 'Could not login'
            self.logs(info)

    #用户登出
    def logout(self):
        self.conn.logout()
        info = 'User {0} logout'.format(self.username)
        self.logs(info)

    #获取邮箱目录(utf-7)
    def getmaildir(self):
        list = self.conn.list()
        maildirlist = []
        for dir in list[1]:
            dir = dir.decode('utf-8').split('"')[3].strip()
            maildirlist.append(dir)
        info = 'User {0} has {1}'.format(self.username,(",".join(maildirlist)))
        self.logs(info)
        return maildirlist

    #获取邮箱目录
    def getmaildir2(self):
        list = self.conn.list()
        maildirlist = []
        for dir in list[1]:
            dir = imap_utf7.decode(dir).split('"')[3].strip()
            maildirlist.append(dir)
        info = 'User {0} has {1}'.format(self.username, (",".join(maildirlist)))
        self.logs(info)
        return maildirlist

    #获取邮件列表
    def getmaillist(self,dir):
        self.dir = dir
        results, message = self.conn.select(self.dir)
        # print(message[0].decode('utf-8'))
        type, data = self.conn.search(None,'ALL')
        info = 'The total number of {0} is {1}'.format(self.dir,message[0].decode('utf-8'))
        return data[0].split()

    #获取邮件主题
    def getsubject(self,msgid):
        self.msgid = msgid
        type, content = self.conn.fetch(self.msgid,'(RFC822)')
        m = email.message_from_bytes(content[0][1])
        if m.get('subject'):
            subject = m.get('subject')
        else:
            subject = '无主题'
        decode_h = email.header.decode_header(subject)
        if decode_h[0][1]:
            sub = decode_h[0][0].decode(decode_h[0][1],'ignore')
        else:
            sub = decode_h[0][0]
        return sub

    #获取邮件时间
    def getmaildate(self,msgid):
        self.msgid = msgid
        type, content = self.conn.fetch(self.msgid, '(RFC822)')
        m = email.message_from_bytes(content[0][1])
        print(m.get('date'))

    #获取邮件eml内容
    def getemlcontent(self,msgid):
        self.msgid = msgid
        type, content = self.conn.fetch(self.msgid, '(RFC822)')
        m = email.message_from_bytes(content[0][1])
        return m[0][1]






user1 = MyImap('10.1.50.64','user1@test.com','q1w2e3r4t5y6')
user1.login()

user1.logout()
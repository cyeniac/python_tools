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



user1 = MyImap('10.1.50.64','user1@test.com','q1w2e3r4t5y6')
user1.login()

user1.logout()
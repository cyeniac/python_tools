#!/usr/bin/env python
#coding:utf-8

"""
Author:Yang Chen
Department:Secure Mail Business Department


"""




import os
import sys
import getopt
import commands
import platform
import socket
import time

#########################################################################
#外部参数获取(未带参数运行脚本返回help信息未解决)
def usage():
	print "use: get.py -d main.test.cn"
	print "use: get.py --domain main.test.cn"
try:
	opts,args = getopt.getopt(sys.argv[1:],"hd:",["help","domain="])
except:
	sys.exit()

#遍历选项参数，将用户自定义参数赋值给自定义的变量
for key,value in opts:
	if key in ("-h","--help"):
		usage()
		sys.exit()
	if key in ("-d","--domain"):
		domain = value

##########################################################################

#获取主机名
myname = socket.getfqdn(socket.gethostname())

##########################################################################
#当前脚本路径
home_dir = os.getcwd()
#函数模块位置
path = home_dir+'/functions/'
sys.path.append(path)
from disk_partition import *
from get_ip_address import *
from get_port_status import *
from get_cpu_rate import *
from get_mem_rate import *
from get_loadavg_rate import *
from get_uptime import *
from recent_log_file import *
#########################################################################
#分割符号
slip = "=" * 30
spack = "\n\n\n\n"
#BUG
intranet_ip = get_intranet_address('eth0')
extranet_ip = get_extranet_address(domain)


#########################################################################


#创建巡检报告
freport = open("report.txt","wt")

#########################################################################


#获取主机名，域名，IP地址
print >> freport,slip+"主机名域名IP地址"+slip
print >> freport,"主机名:"+myname
print >> freport,"局域网IP地址:"+intranet_ip
print >> freport,"外网IP地址:"+extranet_ip
print >> freport,spack

#获取系统类型	
(status, output) = commands.getstatusoutput('cat /etc/.productinfo')
print >> freport,slip+"当前操作系统类型"+slip
print >> freport,output+spack

#获取系统内核,system_uname为数组
system_uname = platform.uname()
system_kernel = system_uname[0]+system_uname[2]
print >> freport,slip+"当前操作系统内核"+slip
print >> freport,system_kernel+spack

#获取邮件平台版本
(status, output) = commands.getstatusoutput('cat /etc/.productinfo.nsmail')
print >> freport,slip+"当前邮件系统版本"+slip
	#可以通过以下方式拆分为数组，输出所需要的内容
	#mail = output.split('\n'),
	#print >> freport,mail[0]
print >> freport,output+spack

#获取磁盘分区情况
(status, output) = commands.getstatusoutput('fdisk -l')
print >> freport,slip+"当前磁盘分区情况"+slip
print >> freport,output+spack

#获取分区使用情况
print >> freport, slip+"磁盘分区使用情况"+slip
for disk_info in disk_partition():
	print >> freport,disk_info
print >> freport,spack

#获取邮件端口状态
print >> freport,slip+"邮件涉及端口状态"+slip
print >> freport,get_port_status(intranet_ip,80)
print >> freport,get_port_status(intranet_ip,443)
print >> freport,get_port_status(intranet_ip,25)
print >> freport,get_port_status(intranet_ip,465)
print >> freport,get_port_status(intranet_ip,143)
print >> freport,get_port_status(intranet_ip,993)
print >> freport,get_port_status(intranet_ip,110)
print >> freport,get_port_status(intranet_ip,995)
print >> freport,get_port_status(intranet_ip,587)
print >> freport,spack

#获取主要服务状态
(status, output) = commands.getstatusoutput('service cs2cmail status')
print >> freport,slip+"主要服务运行状态"+slip
print >> freport,output+spack

#获取CPU，负载，内存使用率
print >> freport,slip+"当前系统状态信息"+slip
print >> freport,get_cpu_rate()
print >> freport,get_mem_rate()
print >> freport,get_loadavg_rate()
print >> freport,get_uptime()
print >> freport,spack

#获取最近日志文件
print >> freport,slip+"近期邮件系统日志"+slip
print >> freport,"    日志名称"+"\t\t"+"日志大小"
for log_file in recent_log_file():
	print >> freport,log_file
print >> freport,spack





freport.close()


	

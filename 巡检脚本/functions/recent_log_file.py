#!/usr/bin/env python
#coding:utf-8
import os
import sys
import commands
import string

def recent_log_file():
	#通过系统命令按时间列出详细日志文件
	(status, output) = commands.getstatusoutput('ls -l -t --color=auto  /var/log/maillogold')
	#将返回结果以换行符分割形成列表存至line
	line = output.split('\n')
	#定义log_list用来筛选列表(其实就是删除第一行的"总容量 ...K")
	log_list = []
	for l in line:
        	if not l.startswith("-rw-r--r--"):
	                continue
	        log_list.append(l)

	#获取所有日志文件的个数
	list_number = len(log_list)
	#定义一个新列表用来存放最近几天的日志文件列表，如果小于10天的日志都列出来
	new_log_list = []
	#格式输出列表
	display_list = []
	if list_number < 10:
	        for i in range(list_number):
	                new_log_list.append(log_list[i])
			log_name = new_log_list[i].split()[8]
			log_size = round((string.atoi(new_log_list[i].split()[4]))/1024/1024.0,2)
			tmp_list = log_name+"\t"+str(log_size)+"M"
			display_list.append(tmp_list)
		return display_list
	
	else:
	        for i in range(10):
	                new_log_list.append(log_list[i])
			log_name = new_log_list[i].split()[8]
                        log_size = round((string.atoi(new_log_list[i].split()[4]))/1024/1024.0,2)
			tmp_list = log_name+"\t"+str(log_size)+"M"
                        display_list.append(tmp_list)
                return display_list


#print recent_log_file()

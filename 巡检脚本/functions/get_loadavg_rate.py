#!/usr/bin/env python
# -*- coding:utf8 -*-

def get_loadavg_rate():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    loadavg['nr']=con[3]
    loadavg['last_pid']=con[4]
    return "1分钟内的平均负载为"+str(loadavg['lavg_1'])+"\n"+"5分钟内的平均负载为"+str(loadavg['lavg_5'])+"\n"+"15分钟内的平均负载为"+str(loadavg['lavg_15'])

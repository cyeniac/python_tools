#!/usr/bin/env python
# -*- coding:utf8 -*-
def get_uptime():
    uptime = {}
    f = open("/proc/uptime")
    con = f.read().split()
    f.close()
    all_sec = float(con[0])
    MINUTE,HOUR,DAY = 60,3600,86400
    uptime['day'] = int(all_sec / DAY )
    uptime['hour'] = int((all_sec % DAY) / HOUR)
    uptime['minute'] = int((all_sec % HOUR) / MINUTE)
    uptime['second'] = int(all_sec % MINUTE)
    uptime['Free rate'] = float(con[1]) / float(con[0])
    return "该系统已经运行："+str(uptime['day'])+"天"+str(uptime['hour'])+"小时"+str(uptime['minute'])+"分钟"+str(uptime['second'])+"秒。"




#print get_uptime()

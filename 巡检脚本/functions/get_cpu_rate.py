#!/usr/bin/env python
# -*- coding:utf8 -*-
 
def get_cpu_rate():
    import time
    def cpu_r():
        f = open("/proc/stat","r")
        for f_line in f:
            break
        f.close()
        f_line = f_line.split(" ")
        f_line_a=[]
        for i in f_line:
            if i.isdigit():
                i=int(i)
                f_line_a.append(i)
        total = sum(f_line_a)
        idle = f_line_a[3]
        return total,idle
 
    total_a,idle_a=cpu_r()
    time.sleep(2)
    total_b,idle_b=cpu_r()
 
    sys_idle = idle_b - idle_a
    sys_total = total_b - total_a
    sys_us = sys_total - sys_idle
 
    cpu_a = round((float(sys_us)/sys_total)*100,2)
    return "CPU利用率："+str(cpu_a)+"%"

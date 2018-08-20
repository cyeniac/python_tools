#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import sys

def get_mem_rate():
	mem = {}
	f = open("/proc/meminfo")
	lines = f.readlines()
	f.close()
	for line in lines:
		if len(line) < 2: 
			continue
		name = line.split(':')[0]
		var = line.split(':')[1].split()[0]
		mem[name] = long(var) * 1024.0
	mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']

	mem_rate = round(float(mem['MemUsed']/mem['MemTotal'])*100,2)
    	return "内存使用率："+str(mem_rate)+"%"


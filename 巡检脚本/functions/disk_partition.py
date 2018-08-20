#!/usr/bin/env python
#coding:utf-8
#/dev/shm这个设备非硬盘目录，在内存中，因此无法与df -h结果一致。

import os
#分析当前系统磁盘信息
def disk_partition():
	#可用的文件系统类型
	phydevs = []
	#默认情况下只会显示本地磁盘挂载信息，如需显示nfs挂载信息需修改/etc/filesystems文件，添加nfs记录
	f1 = open("/proc/filesystems","r")
	for line in f1:
		#如果不是以nodev开头的字符串
		if not line.startswith("nodev"):
			#对该行字符串进行分割并添加到列表phydevs中
			phydevs.append(line.strip())
#	return phydevs

#print disk_partition()


	f2 = open("/etc/filesystems","r")
	for line in f2:
		if not line.startswith("nodev") and line.strip() not in phydevs:
			phydevs.append(line.strip())

#	return phydevs

#print disk_partition()


#	return phydevs

	#将可用的磁盘分区存储至retlist列表中
	retlist = []
	f3 = open('/etc/mtab',"r")
	for line in f3:
		#如果该行为空或者以none开头的字符串则不再执行以下语句直接循环下一行
		if line.startswith('none'):


			continue

		#将不是以none开头的行转换成列表赋给tmp
		tmp = line.split()
		#如果文件系统的类型不在之前的phydevs类型内直接循环下一行		
		if tmp[2] not in phydevs:
			continue

#		retlist.append(tmp)
#	return retlist

		#删除列表的后三个元素(无用的)
		tmp.pop()
		tmp.pop()
		tmp.pop()


		#符合要求的分区容量信息
		#tmp[1]为挂载点
		st = os.statvfs(tmp[1])
		#可用容量
		free = round((st.f_bavail * st.f_frsize)/1024/1024/1024.0,2)
		#全部容量
		total = round((st.f_blocks * st.f_frsize)/1024/1024/1024.0,2)
		#已用容量
		used = round((st.f_blocks - st.f_bfree) * st.f_frsize/1024/1024/1024.0,2)
		#使用百分比
		try:
			percent = ret = (float(used) / total) * 100
		except ZeroDivisionError:
			percent = 0
		#插入一个值得时候可以用list.append()函数，多个值用list.extend(),注意[]
		tmp.extend([total,used,free,round(percent,1)])
		#不能用以下的方法插入值，会越界的
#		tmp[6] = total
#		tmp[7] = used
#		tmp[8] = free
#		tmp[9] = round(percent,1)

		#将符合要求的添加到列表retlist中,得到一个二维数组
		retlist.append(tmp)
#	return retlist



	#获取该二维列表的长度（分区个数）
	l = len(retlist)
	#定义一个列表用来存储自定义格式的磁盘信息
	disklist = []
	for n in range(l): 
		m = n + 1
		disk = "文件系统"+str(m)+"："+str(retlist[n][0])+",挂载点为："+str(retlist[n][1])+",文件系统类型为："+str(retlist[n][2])+",空间总量为："+str(retlist[n][3])+"G,已用"+str(retlist[n][4])+"G,剩余"+str(retlist[n][5])+"G,空间使用率为"+str(retlist[n][6])+"%。"
		disklist.append(disk)
	return disklist


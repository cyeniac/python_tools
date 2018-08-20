#!/usr/bin/env python
import socket
import fcntl
import struct

def get_intranet_address(ifname):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	inet = fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))
	ret = socket.inet_ntoa(inet[20:24])
	return ret

def get_extranet_address(domain):
	try:
		return  socket.getaddrinfo(domain,'http')[0][4][0]
	except:
		return "No DNS server for the domain name resolution"


#print get_extranet_address('mail.gov.cn')
    

#!/usr/bin/env python

import os
import socket
from get_ip_address import *


def get_port_status(ip,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
        	s.connect((ip,int(port)))
		s.shutdown(2)
		return '%d is open' % port
		
	except:
		return '%d is down' % port


#!/usr/bin/python
import re
ipstyle='10.22.201'
def GetCommand(code):
	if code=='1':
		return 'Log out'
	if code=='23':
		return 'Receive message'
	if code=='88':
		return 'Download group friend'
	if code=='103':
		return 'Signature operation'
	if code=='129':
		return 'Get status of friend'
	if code=='13':
		return 'Set status'
	if code=='60':
		return 'Group name operation'
	if code=='29':
		return 'Request KEY'
	if code=='39':
		return 'Get friend online'
	if code=='62':
		return 'MEMO Opration'
	if code=='2':
		return 'Heart Message'
	if code=='92':
		return 'Get leave'
	if code=='101':
		return 'Request extra information'
	if code=='60':
		return 'Group name operation'
	if code=='181':
		return 'Get friend\'s status of group'
	return 'UNKNOW :'+code
f=open('/tmp/oicq','r')
ip_pattern=re.compile(r'[\d.,]+')
qqid_pattern=re.compile(r'(?<=\s)[\d]+(?=\s)')
command_pattern=re.compile(r'[\d]+$')
for line in f:
	ips=ip_pattern.search(line).group()	
	qqid=qqid_pattern.search(line).group()
	command=command_pattern.search(line).group()
	ip=ips.split(',')
	ipstyle_pattern=re.compile(ipstyle+'*')
	if ipstyle_pattern.search(ip[0]):
		src_ip=ip[0]
	else:
		src_ip=ip[1]
	print(src_ip+':'+qqid+"\t"+GetCommand(command))


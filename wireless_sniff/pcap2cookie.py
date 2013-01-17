#!/usr/bin/python
#This script is designed for find cookies and releted host from a .pcap of .cap files 
#This script need the 'tshark' software,which is the console version of 'wireshark'.
import re
import os
#Configure dir & filetype
dir='./'
filetype='cap'
#end od configure

file_list=[file_name for file_name in os.listdir(dir) if file_name.endswith(filetype)]
for file_name in file_list:
	os.system('tshark -r '+dir+file_name+' -R \'http.cookie\' -T fields -e http.host -e http.cookie >>'+dir+'result.txt')



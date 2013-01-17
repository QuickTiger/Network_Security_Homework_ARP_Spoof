import re
import os 
from os import system
system("etterlog -p /var/sec/info.eci >/var/sec/log_")
ori=open('/var/sec/log_','r')
out=open('/var/sec/log','w')
for line in ori:
	if line.find("USER")>0:
		if line.find("etterlog")==-1:
		#	print(line)
			out.write(line)
ori.close()
out.close()
system("rm /var/sec/log_")

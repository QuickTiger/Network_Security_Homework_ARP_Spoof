#!/usr/bin/python
import sqlite3
data_base='./cookie.db'
def sql_command(data_base,command):
	cu=sqlite3.connect(data_base)
	cx=cu.cursor()
	try:
		cx.execute(command)
		cx.commit()
	except Exception as e:
		print(e)
		return False
	feed_back=cx.fetchall()
	cx.close()
	cu.close()
	return feed_back
print(sql_command(data_base,raw_input()))		

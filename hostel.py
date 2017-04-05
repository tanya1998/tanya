#!/usr/bin/python
import MySQLdb
from datetime import datetime
db=MySQLdb.connect(host="localhost",user="root",passwd="raspberry",db="mess")
cur=db.cursor()
#get rfid value
rfid='2016019'
cur.execute("SELECT * FROM hostel WHERE RFid='RF2016019'")
for row in cur.fetchall():
	if row[6]==1:
		cur.execute("UPDATE hostel SET Entry=0, ExitTime=1 WHERE RFid='RF2016019'")
		db.commit()
	else:
		cur.execute("UPDATE hostel SET Entry=1, ExitTime=0 WHERE RFid='RF2016019'") 
		db.commit()
db.close()

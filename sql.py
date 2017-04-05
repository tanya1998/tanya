#!/usr/bin/python
import MySQLdb
from datetime import datetime

h=datetime.now().strftime('%H')
m1=datetime.now().strftime('%M')
s=datetime.now().strftime('%S')
y=datetime.now().strftime('%Y')
print y
m=datetime.now().strftime('%m')
print m
d=datetime.now().strftime('%d')
print d
check = "false"

#print str(a)
#print str(b)
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="raspberry",  # your password
                     db="mess")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT *  FROM mess WHERE RFid='RF2016108'")

try:
    cur.execute("INSERT INTO mess VALUES (1,'Tanya Raj', 'tanya16108@iiitd.ac.in','R1002',,'2016108',1700,CURDATE(),'2017-03-30',20,20,20,20,'false')")
    db.commit()
    print "Data commited"
except:
    print"Error"
    db.rollback()
#with db:
#    cur.execute("INSERT INTO tempdat VALUES (CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'kitchen', 21)")
# print all the first cell of all the rows
for row in cur.fetchall():
    b =str(row[6])
    a= b.index('-');
    z= b.rfind('-');
    y1=b[0:a]
    print y1
    m1=b[a+1:z]
    print m1
    d1=b[z+1: ]
    print d1         		   
    c =str(row[7])
    a= c.index('-');
    z= c.rfind('-');
    y2=c[0:a]
    print y2 
    m2=c[a+1:z]
    print m2
    d2=c[z+1: ]
    print d2
db.close()
if(y1==y and y2==y and y2==y1 and m1==m and m2==m and m1==m2 and d1<=d and d2>=d):
    check="True"


if(check == "True"):
   db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="raspberry",  # your password
                     db="mess")        # name of the data base

   cur = db.cursor()
   br="False"
   l ="False"
   et="False"
   din="False"
   s1 = h+':'+m1+':'+s
   s1 = "08:15:00"
   cur.execute ("SELECT * FROM time1 WHERE sb<=%s AND eb>=%s",(s1,s1))
   for rows in cur.fetchall():
       print str(rows[0])
       if(str(rows[0])=="Breakfast"):
	     br = "True"
       if(str(rows[0])=="lunch"):
             l = "True"
       if(str(rows[0])=="dinner"):
             et = "True"
       if(str(rows[0])=="eveningtea"):
             din = "True"
   new = 0
   cur.execute("SELECT * FROM mess WHERE RFid ='RF2016108'")
   for rows in cur.fetchall():
          if(br =="True"):
               new = rows[8]
	       new =new-1
               print new
               cur.execute("UPDATE mess SET breakfast =%s WHERE RFid ='RF2016108'",new)
               db.commit()
          if(l =="True"):
               new = rows[9]
               new =new-1
               cur.execute("UPDATE mess SET lunch = %s WHERE RFid ='RF2016108'",new)
               db.commit()
          if(et =="True"):
               new = rows[10]
               new =new-1
               cur.execute("UPDATE mess SET eveningtea =%s WHERE RFid ='RF2016108'",new)
               db.commit() 
          if(din =="True"):
               new = rows[11]
               new =new-1
               cur.execute("UPDATE mess SET dinner =%s WHERE RFid ='RF2016108'",new)
               db.commit() 
   db.close()    

      



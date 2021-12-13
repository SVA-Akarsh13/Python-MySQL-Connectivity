import mysql.connector
from hashlib import md5
from time import time
import string
import random
import time
from time import mktime
from datetime import datetime


conn = mysql.connector.connect(user='root', password='Admin', host='127.0.0.1', port=3306, database='testdb', auth_plugin='mysql_native_password')
cursor = conn.cursor()

dates=[]
def randomDate(start, end):
    
    frmt = '%d-%m-%Y %H:%M:%S'
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + random.random() * (etime - stime)
    dt = datetime.fromtimestamp(time.mktime(time.localtime(ptime)))
    return str(dt)

for i in range(0,10):
    dates.append(randomDate("20-01-2018 13:30:00","23-01-2018 03:30:00"))
    print(dates)

count=0
DEVICE_ID=[]
DEVICE_NAME=[]
BARCODE=[]
PRICE=[]
STOCK=[]
SIZE=[]
param_list=[]
while(count<10):
    N=6
    DEVICE_ID.append( ''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    DEVICE_NAME.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    BARCODE.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    PRICE.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    STOCK.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    SIZE.append(''.join(random.choices(string.ascii_uppercase+string.digits, k=N)))
    dates.append(randomDate("20-01-2018 13:30:00","23-01-2018 03:30:00"))
    count+=1
    param_list.append(' '.join(DEVICE_ID+DEVICE_NAME+BARCODE+PRICE+STOCK+SIZE+dates))

#Tuples_Execution

Device_id = tuple(DEVICE_ID)
Device_name = tuple(DEVICE_NAME)
barcode = tuple(BARCODE)
price = tuple(PRICE)
stock = tuple(STOCK)
size = tuple(SIZE)
print(Device_id,Device_name,barcode,price,stock,size)

#Creating a table and inserting values

sql ='''CREATE TABLE IF NOT EXISTS DEVICE(
   DEVICE_ID CHAR(20),
   DEVICE_NAME CHAR(20),
   BARCODE CHAR(7),
   PRICE CHAR(10),
   STOCK CHAR(8),
   SIZE CHAR(10),
   DATES VARCHAR(20)
)'''
cursor.execute(sql)

sql = "INSERT INTO Device(DEVICE_ID, DEVICE_NAME, BARCODE, PRICE, STOCK, SIZE,dates) VALUES(%s,%s,%s,%s,%s,%s,%s)"
cnt=0

for param in param_list:
    values = (DEVICE_ID[cnt],DEVICE_NAME[cnt],BARCODE[cnt],PRICE[cnt],STOCK[cnt],SIZE[cnt],dates[cnt])
    cursor.execute(sql, values)
    cnt+=1
    
conn.commit()
print("List of tables: ")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

conn.close()

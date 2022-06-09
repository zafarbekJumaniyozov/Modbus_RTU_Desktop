import random
import mysql.connector
strl=""
def qrCode():
 # x=input()
 x = 'abc'
 l=random.randrange(1,1000000)
 strl=str(l)
 print( x+strl)
 uzunlik=len(strl)
 qrCode=" "
 if (uzunlik ==1):
     qrCode=x+"00000"+strl
     print(qrCode)
 elif(uzunlik==2):
     qrCode = x + "0000" + strl
     print(qrCode)
 elif(uzunlik==3):
     qrCode = x + "000" + strl
     print(qrCode)
 elif(uzunlik==4):
     qrCode = x + "00" + strl
     print(qrCode)
 elif(uzunlik==5):
     qrCode = x + "0" + strl
     print(qrCode)
 elif(uzunlik==6):
     qrCode = x  + strl
     print(qrCode)


 print(uzunlik)
qrCode()



mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='tadbir')
mycursor = mydb.cursor()
motorSensorSql = "INSERT INTO name(id,name)VALUES (%s,%s)"
valmotorSensor = (1, "ggdd")
mycursor.execute(motorSensorSql, valmotorSensor)

mydb.commit()
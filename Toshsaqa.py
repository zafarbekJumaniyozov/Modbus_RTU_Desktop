from tkinter import *
import mysql.connector
import time
import serial
import minimalmodbus
from time import sleep
import datetime

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water' )
mycursor=mydb.cursor()



mycursor.execute("SELECT comport FROM s_obekt where indeks='Xiva'")
exCom = str(mycursor.fetchone())
comport='COM'+exCom[1:len(exCom)-2]


motorKalit1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorKalit1.serial.baudrate = 9600
# baudrate
motorKalit1.serial.bytesize = 8
motorKalit1.serial.parity   = serial.PARITY_NONE
motorKalit1.serial.stopbits = 1
motorKalit1.serial.timeout  =2      # seconds
motorKalit1.address         = 1   #Motor qo'shish  uchun Xiva

motorKalit2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorKalit2.serial.baudrate = 9600
# baudrate
motorKalit2.serial.bytesize = 8
motorKalit2.serial.parity   = serial.PARITY_NONE
motorKalit2.serial.stopbits = 1
motorKalit2.serial.timeout  =2      # seconds
motorKalit2.address         = 2  #Motor datchiklar 4, 3, 2   uchun Xiva


motorsensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorsensor1.serial.baudrate = 9600
# baudrate
motorsensor1.serial.bytesize = 8
motorsensor1.serial.parity   = serial.PARITY_NONE
motorsensor1.serial.stopbits = 1
motorsensor1.serial.timeout  =2      # seconds
motorsensor1.address         = 3
motorsensor1.mode = minimalmodbus.MODE_RTU

motorsensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorsensor2.serial.baudrate = 9600
# baudrate
motorsensor2.serial.bytesize = 8
motorsensor2.serial.parity   = serial.PARITY_NONE
motorsensor2.serial.stopbits = 1
motorsensor2.serial.timeout  =2      # seconds
motorsensor2.address         = 4 # input yozilgandan kelgani
motorsensor2.mode = minimalmodbus.MODE_RTU


motorsensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorKalit1.serial.baudrate = 9600
# baudrate
motorsensor3.serial.bytesize = 8
motorsensor3.serial.parity   = serial.PARITY_NONE
motorsensor3.serial.stopbits = 1
motorsensor3.serial.timeout  =2     # seconds
motorsensor3.address         = 5    #sensor 5, 6, 7  uchun Xiva
motorsensor3.mode = minimalmodbus.MODE_RTU


motorsensor4 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorKalit1.serial.baudrate = 9600
# baudrate
motorsensor4.serial.bytesize = 8
motorsensor4.serial.parity   = serial.PARITY_NONE
motorsensor4.serial.stopbits = 1
motorsensor4.serial.timeout  =2     # seconds
motorsensor4.address         = 6
motorsensor4.mode = minimalmodbus.MODE_RTU

motorsensor5 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorsensor5.serial.baudrate = 9600
# baudrate
motorsensor5.serial.bytesize = 8
motorsensor5.serial.parity   = serial.PARITY_NONE
motorsensor5.serial.stopbits = 1
motorsensor5.serial.timeout  =2
motorsensor5.address         = 7
motorsensor5.mode = minimalmodbus.MODE_RTU

motorsensor6 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
motorsensor6.serial.baudrate = 9600
# baudrate
motorsensor6.serial.bytesize = 8
motorsensor6.serial.parity   = serial.PARITY_NONE
motorsensor6.serial.stopbits = 1
motorsensor6.serial.timeout  =2
motorsensor6.address         = 8
motorsensor6.mode = minimalmodbus.MODE_RTU

watersensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
watersensor1.serial.baudrate = 9600
# baudrate
watersensor1.serial.bytesize = 8
watersensor1.serial.parity   = serial.PARITY_NONE
watersensor1.serial.stopbits = 1
watersensor1.serial.timeout  =2
watersensor1.address         = 9
watersensor1.mode = minimalmodbus.MODE_RTU

watersensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
watersensor2.serial.baudrate = 9600
# baudrate
watersensor2.serial.bytesize = 8
watersensor2.serial.parity   = serial.PARITY_NONE
watersensor2.serial.stopbits = 1
watersensor2.serial.timeout  =2
watersensor2.address         = 10
watersensor2.mode = minimalmodbus.MODE_RTU

watersensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
watersensor3.serial.baudrate = 9600
# baudrate
watersensor3.serial.bytesize = 8
watersensor3.serial.parity   = serial.PARITY_NONE
watersensor3.serial.stopbits = 1
watersensor3.serial.timeout  =2
watersensor3.address         = 11
watersensor3.mode = minimalmodbus.MODE_RTU

# seconds


# this is the slave address number
#motorKalit1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode




def on1():
    motorKalit1.write_register(2, 0x0200)
    motorKalit1.write_register(1, 0x0100)


    labOldsensor1=float(labelsensor1.cget("text"))
    labelOldsensor1=Label(window,text=str(labOldsensor1),bg="grey",width=20)
    labelOldsensor1.grid(row=3, column=3)


def on2():
    motorKalit1.write_register(1, 0x0200)
    motorKalit1.write_register(2, 0x0100)



def on3():
    motorKalit1.write_register(4, 0x0200)
    motorKalit1.write_register(3, 0x0100)


def on4():

    motorKalit1.write_register(3, 0x0200)
    motorKalit1.write_register(4, 0x0100)


def on5():
    motorKalit1.write_register(6, 0x0200)
    motorKalit1.write_register(5, 0x0100)


def on6():
    motorKalit1.write_register(5, 0x0200)
    motorKalit1.write_register(6, 0x0100)



def on7():
    motorKalit1.write_register(8, 0x0200)
    motorKalit1.write_register(7, 0x0100)


def on8():
    motorKalit1.write_register(7, 0x0200)
    motorKalit1.write_register(8, 0x0100)


def on9():
    motorKalit2.write_register(2, 0x0200)
    motorKalit2.write_register(1, 0x0100)


def on10():
    motorKalit2.write_register(1, 0x0200)
    motorKalit2.write_register(2, 0x0100)


def on11():
    motorKalit2.write_register(4, 0x0200)
    motorKalit2.write_register(3, 0x0100)


def on12():
    motorKalit2.write_register(3, 0x0200)
    motorKalit2.write_register(4, 0x0100)


def off1():
    motorKalit1.write_register(1, 0x0200)
    motorKalit1.write_register(2, 0x0200)


def off2():
    motorKalit1.write_register(3, 0x0200)
    motorKalit1.write_register(4, 0x0200)


def off3():
    motorKalit1.write_register(5, 0x0200)
    motorKalit1.write_register(6, 0x0200)

def off4():
    motorKalit1.write_register(7, 0x0200)
    motorKalit1.write_register(8, 0x0200)

def off5():
    motorKalit2.write_register(1, 0x0200)
    motorKalit2.write_register(2, 0x0200)


def off6():
    motorKalit2.write_register(3, 0x0200)
    motorKalit2.write_register(4, 0x0200)



def water_sensor():

    sensor9a=str(watersensor1.read_register(1,0,3))

    sensor9=float(int(sensor9a[0:len(sensor9a)-1])/100)
    labelIN.configure(text=sensor9 )

    sensorSql9 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valsensor9 = (1, 7, 1, sensor9)
    mycursor.execute(sensorSql9, valsensor9)
    mydb.commit()
#sensor10 uchun
    sensor10a=str(watersensor2.read_register(1,0,3))

    sensor10=float(int(sensor10a[0:len(sensor10a)-1])/100)
    labelOut1.configure(text=sensor10 )
    sensorSql10 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valsensor10 = (1, 6, 1, sensor10)
    mycursor.execute(sensorSql10, valsensor10)
    mydb.commit()

    # sensor11 uchun
    sensor11a=str(watersensor3.read_register(1,0,3))
    sensor11=float(int(sensor11a[0:len(sensor11a)-1])/100)
    labelOut2.configure(text=sensor11 )
    #Bazaga yozish
    sensorSql11="INSERT INTO water_sensor(asos_id,sensor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valsensor11 = (1, 5, 1,sensor11)
    mycursor.execute(sensorSql11,valsensor11)
    mydb.commit()




    labelOut1.after(2000,water_sensor)
def motor_sensor():
    # sensoor1
    # past_suv=int(3200)
    sensor1a = str(motorsensor1.read_register(1, 0, 3))
    pastki_sath1 = 2.35  # bazadan sathni olish kerak vazifa


    sensor1 =  float(int(sensor1a[0:len(sensor1a) - 1]) / 100)
    labelsensor1.configure(text=sensor1)
    sensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor1 = (1, 1, 1, sensor1)
    mycursor.execute(sensorSql1, valSensor1)
    mydb.commit()

    # Sensor2
    sensor2a = str(motorsensor2.read_register(1, 0, 3))
    pastki_sath2 = 2.31
    sensor2 = float(int(sensor2a[0:len(sensor2a) - 1]) / 100)

    labelsensor2.configure(text=sensor2)
    # 2-motorning sensorindagi malumoti yozish
    sensorSql2 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor2 = (1, 2, 1, sensor2)
    mycursor.execute(sensorSql2, valSensor2)
    mydb.commit()
    # sensor3

    sensor3a = str(motorsensor3.read_register(1, 0, 3))
    pastki_sath3 = 2.25
    sensor3 =  float(int(sensor3a[0:len(sensor3a) - 1]) / 100)
    labelsensor3.configure(text=sensor3)

 #1-motorning sensorindagi malumoti yozish

    # 3-motorning sensorindagi malumoti yozish
    sensorSql3 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor3 = (1, 3, 1, sensor3)
    mycursor.execute(sensorSql3, valSensor3)
    mydb.commit()



    sensor4a = str(motorsensor4.read_register(1, 0, 3))
    pastki_sath4 = 2.25

    sensor4 =  float(int(sensor4a[0:len(sensor4a) - 1]) / 100)
    labelsensor4.configure(text=sensor4)

 #1-motorning sensorindagi malumoti yozish

    # 3-motorning sensorindagi malumoti yozish
    sensorSql4 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor4 = (1, 3, 1, sensor4)
    mycursor.execute(sensorSql4, valSensor4)
    mydb.commit()



    sensor5a = str(motorsensor5.read_register(1, 0, 3))
    pastki_sath5 = 2.25
    sensor5 = float(int(sensor5a[0:len(sensor5a) - 1]) / 100)
    labelsensor5.configure(text=sensor5)
 #1-motorning sensorindagi malumoti yozish

    # 3-motorning sensorindagi malumoti yozish
    sensorSql5 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor5 = (1, 3, 1, sensor5)
    mycursor.execute(sensorSql5, valSensor5)
    mydb.commit()



    sensor6a = str(motorsensor6.read_register(1, 0, 3))
    pastki_sath6 = 2.25
    sensor6 =  float(int(sensor6a[0:len(sensor6a) - 1]) / 100)
    labelsensor6.configure(text=sensor6)

 #1-motorning sensorindagi malumoti yozish

    # 3-motorning sensorindagi malumoti yozish
    sensorSql6 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor6 = (1, 3, 1, sensor6)
    mycursor.execute(sensorSql6, valSensor6)
    mydb.commit()
    labelsensor1.after((2000,motor_sensor))




window=Tk()
window.title('Toshsaqa')
window.geometry('1200x700')
window.configure(bg="#0099cc")

label=Label(text='Control Motor',fg='orange',bg='blue',width=20,font=('italic',25,'bold')).grid(row=1,column=3,padx=25,pady=6)

label1=Label(text='1',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=3,column=1,padx=3,pady=6)

labelsensor1=Label(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor1.grid(row=3,column=2)

sath1=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=3,column=3)
button11=Button(window,width=5,command=on1,text='tepaga',fg='white',bg='green',font=('italic',14,'bold')).grid(row=3,column=4,padx=3,pady=6)
button12=Button(window,width=5,command=off1,text='stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=3,column=5,padx=3,pady=6)
button13=Button(window,width=5,command=on2,text='pastga',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=3,column=6,padx=3,pady=6)


label2=Button(text='2',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=4,column=1,padx=3,pady=6)
labelsensor2=Label(font=('Arial',20),bg='white',fg='black',width=5,bd=2,
            relief=SUNKEN)
labelsensor2.grid(row=4,column=2)
sath2=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=4,column=3)
button21=Button(window,width=5,command=on3,text='tepaga',fg='white',bg='green',font=('italic',14,'bold')).grid(row=4,column=4,padx=3,pady=6)
button22=Button(window,width=5,command=off2,text='stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=4,column=5,padx=3,pady=6)
button23=Button(window,width=5,command=on4,text='pastga',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=4,column=6,padx=3,pady=6)



label3=Button(text='3',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=5,column=1,padx=3,pady=6)
labelsensor3=Label(font=('Arial',20),text=' ',bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor3.grid(row=5,column=2)
sath3=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=5,column=3)
button31=Button(window,width=5,text='tepaga',command=on5,fg='white',bg='green',font=('italic',14,'bold')).grid(row=5,column=4,padx=3,pady=6)
button32=Button(window,width=5,text='stop',command=off3,fg='white',bg='red',font=('italic',14,'bold')).grid(row=5,column=5,padx=3,pady=6)
button33=Button(window,width=5,text='pastga',command=on6,fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=5,column=6,padx=3,pady=6)


label4=Button(text='4',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=6,column=1,padx=3,pady=6)
labelsensor4=Label(font=('Arial',20),text=' ',bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor4.grid(row=6,column=2)
sath4=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=6,column=3)
button41=Button(window,width=5,text='tepaga',command=on7,fg='white',bg='green',font=('italic',14,'bold')).grid(row=6,column=4,padx=3,pady=6)
button42=Button(window,width=5,text='stop',command=off4,fg='white',bg='red',font=('italic',14,'bold')).grid(row=6,column=5,padx=3,pady=6)
button43=Button(window,width=5,text='pastga',command=on8,fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=6,column=6,padx=3,pady=6)


label5=Button(text='5',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=7,column=1,padx=3,pady=6)
labelsensor5=Label(font=('Arial',20),text=' ',bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor5.grid(row=7,column=2)
sath5=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=7,column=3)
button51=Button(window,width=5,text='tepaga',command=on5,fg='white',bg='green',font=('italic',14,'bold')).grid(row=7,column=4,padx=3,pady=6)
button52=Button(window,width=5,text='stop',command=off3,fg='white',bg='red',font=('italic',14,'bold')).grid(row=7,column=5,padx=3,pady=6)
button53=Button(window,width=5,text='pastga',command=on6,fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=7,column=6,padx=3,pady=6)


label6=Button(text='6',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=8,column=1,padx=3,pady=6)
labelsensor6=Label(font=('Arial',20),text=' ',bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor6.grid(row=8,column=2)
sath6=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=8,column=3)
button61=Button(window,width=5,text='tepaga',command=on5,fg='white',bg='green',font=('italic',14,'bold')).grid(row=8,column=4,padx=3,pady=6)
button62=Button(window,width=5,text='stop',command=off3,fg='white',bg='red',font=('italic',14,'bold')).grid(row=8,column=5,padx=3,pady=6)
button63=Button(window,width=5,text='pastga',command=on6,fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=8,column=6,padx=3,pady=6)


buttonIn=Button(text='kirish',fg='white',bg='blue',width=9,font=('italic',16,'bold')).grid(row=9,column=1,padx=3,pady=6)
buttonOut=Button(text='chiqish1',fg='white',bg='blue',width=9,font=('italic',16,'bold')).grid(row=10,column=1,padx=3,pady=6)
buttonOutPut2=Button(text='chiqish2  ',fg='white',bg='blue',width=10,font=('italic',12,'bold')).grid(row=11,column=1,padx=3,pady=6)



labelIN=Label(text=' ',font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8)
labelIN.grid(row=9,column=2)
labelOut1=Label(text=' ',font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8)
labelOut1.grid(row=10,column=2)

labelOut2=Label(text=' ',font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8)
labelOut2.grid(row=11,column=2)
buttonOnM=Button(text='onM',command=motor_sensor,fg='white',bg='blue',width=7,font=('italic',16,'bold'))
buttonOnM.grid(row=12,column=1,padx=3,pady=6)
buttonOffM=Button(text='offM',fg='white',bg='blue',width=10,font=('italic',12,'bold'))
buttonOffM.grid(row=12,column=2,padx=3,pady=6)

buttonOnW=Button(text='onW',command=water_sensor,fg='white',bg='blue',width=7,font=('italic',16,'bold'))
buttonOnW.grid(row=12,column=3,padx=3,pady=6)
buttonOffW=Button(text='offW',fg='white',bg='blue',width=10,font=('italic',12,'bold'))
buttonOffW.grid(row=12,column=4,padx=3,pady=6)





window.mainloop()


from tkinter import *
import mysql.connector
import time
import serial
import minimalmodbus
from time import sleep
import datetime
import pyautogui
from pyglet.media import player
from setuptools import sic
from tkinter import ttk
import pyglet
#Mysql ulash
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water')
mycursor = mydb.cursor()
#programma qo'yilgan obekt
obekt="Select obekt from setup"
mycursor.execute(obekt)
obekt = mycursor.fetchone()
obekt = str(obekt)[1:(len(obekt) - 3)]
#Comport o'zgartirish
mycursor.execute("SELECT comport FROM s_obekt where indeks='Toshsaqa'")
exCom = str(mycursor.fetchone())
comport = 'COM' + exCom[1:len(exCom) - 2]
#buyruqdagi suv hajmi
buyruqhajmi = "Select kub from asos where obekt_id=%s order by id desc limit 1"
mycursor.execute(buyruqhajmi,[obekt])
buyruqMassiv = mycursor.fetchone()
buyruq1 = str(buyruqMassiv)[1:len(buyruqMassiv) - 3]
print(buyruq1)
#buyruq berilgan sana
sana="Select sana from asos where obekt_id=%s order by id desc limit 1"
mycursor.execute(sana,[obekt])
sana =str( mycursor.fetchone())[19:len(str(mycursor.fetchone())) - 7]
#me'yordan   kop suv o'tish chegarasi
ogoh= "Select ogoh from s_obekt where id=%s "
mycursor.execute(ogoh,[obekt])
ogoh1 = mycursor.fetchone()
ogoh1 = float(str(ogoh1)[1:len(ogoh1) - 3])
#me'yordan  juda kop suv o'tish chegarasi
alarm= "Select alarm from s_obekt where id=%s "
mycursor.execute(alarm,[obekt])
alarm1 = mycursor.fetchone()
alarm1 = float(str(alarm1)[1:len(alarm1) - 3])
#max1-motorniki
max1= "Select max from s_motor where id=1 "
mycursor.execute(max1)
max1 = mycursor.fetchone()
max1 = float(str(max1)[1:len(max1) - 3])
#max2-motorniki
max2= "Select max from s_motor where id=2 "
mycursor.execute(max2)
max2 = mycursor.fetchone()
max2 = float(str(max2)[1:len(max2) - 3])

#max3-motorniki
max3= "Select max from s_motor where id=3 "
mycursor.execute(max3)
max3 = mycursor.fetchone()
max3 = float(str(max3)[1:len(max3) - 3])

#min 1-motorniki
mycursor.execute("SELECT min FROM s_motor where id=1")
pastki_sath1 = str(mycursor.fetchone())
pastki_sath1 = float(pastki_sath1[1:len(pastki_sath1) - 2])
#min 2-motorniki
mycursor.execute("SELECT min FROM s_motor where id=2")
pastki_sath2 = str(mycursor.fetchone())
pastki_sath2 = float(pastki_sath2[1:len(pastki_sath2) - 2])
#min 3-motorniki
mycursor.execute("SELECT min FROM s_motor where id=3")
pastki_sath3 = str(mycursor.fetchone())
pastki_sath3 = float(pastki_sath3[1:len(pastki_sath3) - 2])
print(pastki_sath3)
#min 4-motorniki
mycursor.execute("SELECT min FROM s_motor where id=4")
pastki_sath4 = str(mycursor.fetchone())
pastki_sath4 = float(pastki_sath4[1:len(pastki_sath4) - 2])
print(pastki_sath4)
#min 5-motorniki
mycursor.execute("SELECT min FROM s_motor where id=5")
pastki_sath5 = str(mycursor.fetchone())
pastki_sath5 = float(pastki_sath5[1:len(pastki_sath5) - 2])
#min 6-motorniki
mycursor.execute("SELECT min FROM s_motor where id=6")
pastki_sath6 = str(mycursor.fetchone())
pastki_sath6 = float(pastki_sath6[1:len(pastki_sath6) - 2])
print(pastki_sath6)
global sensr
sensr = 0
global onoff1,onoff2,onoff3, onoff4,onoff5,onoff6,res
res=300
sensor1a = '210'
sensor2a = '250'
sensor3a = '200'
sensor4a = '210'
sensor5a = '250'
sensor6a = '200'
if sensr == 1:
    onoff1 = 0
    onoff2 = 0
    onoff3 = 0
    onoff4 = 0
    onoff5 = 0
    onoff6 = 0

    # client2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    # client2.serial.baudrate = 9600
    # # baudrate
    # client2.serial.bytesize = 8
    # client2.serial.parity = serial.PARITY_NONE
    # client2.serial.stopbits = 1
    # client2.serial.timeout = 2  # seconds
    # client2.address = 4  # Motor datchiklar 4, 3, 2   uchun Xiva
    #

    motorKalit1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorKalit1.serial.baudrate = 9600
    # baudrate
    motorKalit1.serial.bytesize = 8
    motorKalit1.serial.parity = serial.PARITY_NONE
    motorKalit1.serial.stopbits = 1
    motorKalit1.serial.timeout = 2  # seconds
    motorKalit1.address = 1  # Motor qo'shish  uchun Xiva


    motorsensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor1.serial.baudrate = 9600
    # baudrate
    motorsensor1.serial.bytesize = 8
    motorsensor1.serial.parity = serial.PARITY_NONE
    motorsensor1.serial.stopbits = 1
    motorsensor1.serial.timeout = 2  # seconds
    motorsensor1.address = 2
    motorsensor1.mode = minimalmodbus.MODE_RTU

    motorsensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorsensor2.serial.baudrate = 9600
    # baudrate
    motorsensor2.serial.bytesize = 8
    motorsensor2.serial.parity = serial.PARITY_NONE
    motorsensor2.serial.stopbits = 1
    motorsensor2.serial.timeout = 2  # seconds
    motorsensor2.address = 3  # input yozilgandan kelgani
    motorsensor2.mode = minimalmodbus.MODE_RTU

    motorsensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    motorKalit1.serial.baudrate = 9600
    # baudrate
    motorsensor3.serial.bytesize = 8
    motorsensor3.serial.parity = serial.PARITY_NONE
    motorsensor3.serial.stopbits = 1
    motorsensor3.serial.timeout = 2  # seconds
    motorsensor3.address = 4  # sensor 5, 6, 7  uchun Xiva
    motorsensor3.mode = minimalmodbus.MODE_RTU


    watersensor1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor1.serial.baudrate = 9600
    # baudrate
    watersensor1.serial.bytesize = 8
    watersensor1.serial.parity = serial.PARITY_NONE
    watersensor1.serial.stopbits = 1
    watersensor1.serial.timeout = 2
    watersensor1.address = 5
    watersensor1.mode = minimalmodbus.MODE_RTU

    watersensor2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor2.serial.baudrate = 9600
    # baudrate
    watersensor2.serial.bytesize = 8
    watersensor2.serial.parity = serial.PARITY_NONE
    watersensor2.serial.stopbits = 1
    watersensor2.serial.timeout = 2
    watersensor2.address = 6
    watersensor2.mode = minimalmodbus.MODE_RTU

    watersensor3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    watersensor3.serial.baudrate = 9600
    # baudrate
    watersensor3.serial.bytesize = 8
    watersensor3.serial.parity = serial.PARITY_NONE
    watersensor3.serial.stopbits = 1
    watersensor3.serial.timeout = 2
    watersensor3.address = 7
    watersensor3.mode = minimalmodbus.MODE_RTU

else:
    onoff1 = 10 # simulyator
    onoff2 = 10
    onoff3 = 10


# this is the slave address number
# client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode




def ogoh():
    labelin=labelINCub.cget('text')
    if(float(buyruq1)+ogoh1<float(labelin)  and float(labelin)<float(buyruq1)+alarm1):
        player = pyglet.media.Player()
        song = 'ogoh.mp3'
        src = pyglet.media.load(song)
        player.queue(src)
        def play():
            player.play()
        play()
    elif(float(float(buyruq1)+alarm1)<float(labelin)):
        player = pyglet.media.Player()
        song = 'alarm.mp3'
        src = pyglet.media.load(song)
        player.queue(src)

        def play():
            player.play()
        play()
    labelINCub.after(15000, ogoh)

def on1():
    global onoff1
    if onoff1 != 11:


        res = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res == None:
            return
        if sensr != 0:
            try:
                onoff1 = 1
                motorKalit1.write_register(2, 0x0200)
                motorKalit1.write_register(1, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:

          return
    else:
        pyautogui.alert(text="Motor ishlayapti to'xtashini kuting")
        return
    sensorSql = "INSERT INTO asos_motor(asos_id,cm,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valSensor = (1, 20, onoff1, datetime.datetime.now(), 1, 1)
    mycursor.execute(sensorSql, valSensor)
    mydb.commit()

    labOldsensor1 = float(labelsensor1.cget("text"))
    labelOldsensor1 = Label(secondWindow,text=str(labOldsensor1), bg="grey",fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldsensor1.grid(row=3, column=4)
    sath1.configure(text=str(res))
def on2():
    global onoff1
    if onoff1 != 12:
        res2 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res2 == None:
            return
        if sensr != 0:
            try:
                onoff1 = 1
                motorKalit1.write_register(1, 0x0200)
                motorKalit1.write_register(2, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff1 = 12

        onoff1 = 12
    else:
        pyautogui.alert(text="Motor ishlayapti to'xtashini kuting")
        return
    sensorSql = "INSERT INTO asos_motor(asos_id,cm,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valSensor = (1, 20, onoff1, datetime.datetime.now(), 1, 1)
    mycursor.execute(sensorSql, valSensor)
    mydb.commit()
    labOldsensor1 = float(labelsensor1.cget("text"))
    labelOldsensor1 = Label(secondWindow, text=str(labOldsensor1), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldsensor1.grid(row=3, column=4)
    sath1.configure(text=str(res2))
def on3():
    global onoff2
    if onoff2 != 11:

        res21 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 21 == None:
            return
        if sensr != 0:
            try:
                onoff2 = 1
                motorKalit1.write_register(4, 0x0200)
                motorKalit1.write_register(3, 0x0100)
            except:
             pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff2 = 11

        onoff2 = 11
    else:
        pyautogui.alert(text="Motor ishlayapti to'xtashini kuting")
        return

    onoff2=11
    labOldsensor2 = float(labelsensor2.cget("text"))
    labelOldsensor2 = Label(secondWindow, text=str(labOldsensor2),bg="grey",fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldsensor2.grid(row=4, column=4)
    sath2.configure(text=str(res21))
def on4():
    global onoff2
    if onoff2 != 12:

        res22 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 22 == None:
            return
        if sensr != 0:
            try:

                onoff2 = 1
                motorKalit1.write_register(3, 0x0200)
                motorKalit1.write_register(4, 0x0100)
            except:
                pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff2 = 12

        onoff2 = 12
    else:
        pyautogui.alert(text="Motor ishlayapti to'xtashini kuting")
        return

    labOldsensor2 = float(labelsensor2.cget("text"))
    labelOldsensor2 = Label(secondWindow, text=str(labOldsensor2), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldsensor2.grid(row=4, column=4)
    sath2.configure(text=str(res22))
def on5():
    global onoff3
    if onoff3 != 11:

        res31 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 31 == None:
            return
        if sensr != 0:
            try:
                onoff3 = 1
                motorKalit1.write_register(6, 0x0200)
                motorKalit1.write_register(5, 0x0100)
            except:
                  pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

        else:
            onoff3 = 11

        onoff3 = 11
    else:
        pyautogui.alert(text="Motor ishlayapti to'xtashini kuting")
        return
    onoff3=11
    labOldsensor3 = float(labelsensor3.cget("text"))
    labelOldsensor3 = Label(secondWindow, text=str(labOldsensor3), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldsensor3.grid(row=5, column=4)
    sath3.configure(text=str(res31))
def on6():
    global onoff3
    if onoff3 != 12:

        res32 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if 32 == None:
            return
        if sensr != 0:

            try:
                onoff3 = 2
                motorKalit1.write_register(6, 0x0200)
                motorKalit1.write_register(5, 0x0100)
            except:
                pyautogui.alert(text="Signal bo'lmadi qayta urinib ko'ring",title='ogohlantirish',bg='yellow')

        else:
            onoff3 = 12

        onoff3 = 12
    else:
        pyautogui.alert(text="Motor ishlayapti to'xtashini kuting",title='ogohlantirish')
        return

    labOldsensor3 = float(labelsensor3.cget("text"))
    labelOldsensor3 = Label(secondWindow, text=str(labOldsensor3), bg="grey", fg="white",  width=7,font=('italic', 16, 'bold'))
    labelOldsensor3.grid(row=5, column=4)
    sath3.configure(text=str(res32))



def motor_sensor():
    global sensor1a,sensor2a,sensor3a,sensor4a,sensor5a,sensor6a,onoff1,onoff2,onoff3,onoff4,onoff5,onoff6,res
    if sensr == 1:
        try:
         sensor1a = str(motorsensor1.read_register(1, 0, 3))
         labelsensor1.configure(bg='white', fg="black")
        except:
            sensorXatoSql = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valSensorxato = (1, 'Sensor ishlamadi')
            mycursor.execute(sensorXatoSql, valSensorxato)
            sensor1a=labelsensor1.cget('text')
            labelsensor1.configure(bg='black',fg="white")

     #Sensor2
            try:
                sensor2a = str(motorsensor2.read_register(1, 0, 3))
                labelsensor2.configure(bg='white', fg="black")
            except:
                print('d')
                sensorXatoSql2 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
                valSensorxato2 = (2, 'Sensor ishlamadi')
                mycursor.execute(sensorXatoSql2, valSensorxato2)
                sensor2a = labelsensor2.cget('text')
                labelsensor2.configure(bg='black', fg="white")
    #sensor3
            try:
                sensor3a = str(motorsensor3.read_register(1, 0, 3))
                labelsensor3.configure(bg='white', fg="black")
            except:
                sensorXatoSql3 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
                valSensorxato3 = (3, 'Sensor ishlamadi')
                mycursor.execute(sensorXatoSql3, valSensorxato3)
                sensor3a = labelsensor3.cget('text')
                labelsensor3.configure(bg='black', fg="white")


        #sensor3

    sensor1 = round(pastki_sath1 - (float(float(sensor1a) / 100)), 2)
    sensor2 = round(pastki_sath2 - (float(float(sensor2a) / 100)), 2)
    sensor3 = round(pastki_sath3 - (float(float(sensor3a) / 100)), 2)


    #tekshirish sensor1
    if sensor1 > float(pastki_sath1 - 0.2):
        if sensr != 0:
            try:
                onoff1 = 0
                motorKalit1.write_register(1, 0x0200)
            except:
                print(" aaa")
                # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff1 = 10
            sensor1 = pastki_sath1

        if sensor1 < 0.1:
         if sensr != 0:
             try:
                motorKalit1.write_register(2, 0x0200)
                onoff1 = 0
             except:
                 print(" aaa"  )#pyautogui.alert(text="signal yo'q qayta urinib ko'ring")

         else:
            onoff1 = 10
    if (float(sensor1a)>pastki_sath1*1000):
        onoff1=10
        sensor1="0"
    print(onoff1)
    #sensor2
    if sensor2 > float(pastki_sath2 - 0.2):
        if sensr != 0:
            try:
                onoff2 = 0
                motorKalit1.write_register(3, 0x0200)
            except:
               print(" aaa"  )# pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
        else:
            onoff1 = 10
            sensor2 = pastki_sath2
        if sensor2 < 0.1:
            if sensr != 0:
                try:
                    motorKalit1.write_register(4, 0x0200)
                    onoff2 = 0
                except:
                    # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                    print(" aaa")
            else:
                onoff2 = 10
    if (float(sensor2a) > pastki_sath2 * 1000):
        onoff1 = 10
        sensor2 = "0"

    #sensor3
    if sensor3 > float(pastki_sath3 - 0.2) :
        if sensr != 0:
            onoff3 = 0
            try:
                motorKalit1.write_register(5, 0x0200)
            except:
                # pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
              print(" aaa"  )
        else:
            onoff3 = 10
            sensor3 = pastki_sath3

    if (float(sensor3a) > pastki_sath3 * 1000):
        if sensr != 0:
            try:

                motorKalit1.write_register(6, 0x0200)
                onoff1 = 0
            except:
                #pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
                print(" aaa")
        else:
            onoff1 = 10
            sensor3 = "0"



    labelsensor1.configure(text=sensor1)
    labelsensor2.configure(text=sensor2)
    labelsensor3.configure(text=sensor3)
    # 1-motorning sensorindagi malumoti yozish
    sensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor1 = (1, 1, 1, sensor1)
    mycursor.execute(sensorSql1, valSensor1)
    mydb.commit()

    # 2-motorning sensorindagi malumoti yozish
    sensorSql2 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor2 = (1, 2, 1, sensor2)
    mycursor.execute(sensorSql2, valSensor2)
    mydb.commit()

    # 3-motorning sensorindagi malumoti yozish
    sensorSql3 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor3 = (1, 3, 1, sensor3)
    mycursor.execute(sensorSql3, valSensor3)
    mydb.commit()

    labelsensor1.after(3000,motor_sensor)


def off1():

    res = pyautogui.confirm(text='', title='1 - motor harakatini to`xtasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    global onoff1
    if sensr != 0:
        try:
            motorKalit1.write_register(1, 0x0200)
            motorKalit1.write_register(2, 0x0200)
            onoff1 = 0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff1 = 10
    print(onoff1)
def off2():
    res = pyautogui.confirm(text='', title='2 - motor harakatini to`xtotasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        try:
            motorKalit1.write_register(3, 0x0200)
            motorKalit1.write_register(4, 0x0200)
            onoff2=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
     onoff2 = 10
    print(onoff2)

def off3():
    res = pyautogui.confirm(text='STOP', title='3 - motor harakatini to`xtotasizmi ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        try:
            motorKalit1.write_register(5, 0x0200)
            motorKalit1.write_register(6, 0x0200)
            onoff3=0
        except:
            pyautogui.alert(text="signal yo'q qayta urinib ko'ring")
    else:
        onoff3 = 10
    print(onoff3)


def water_sensor():
    farq= "Select farq_sm from s_farq where sensor_id=1 order by id desc limit 1"
    mycursor.execute(farq)
    farqMassiv = mycursor.fetchone()
    farqSath1=int(str(farqMassiv)[1:(len(farqMassiv)-3)])

    farq = "Select farq_sm from s_farq where sensor_id=2 order by id desc limit 1"
    mycursor.execute(farq)
    farqMassiv = mycursor.fetchone()
    farqSath2=int(str(farqMassiv)[1:(len(farqMassiv)-3)])

    farq = "Select farq_sm from s_farq where sensor_id=3 order by id desc limit 1"
    mycursor.execute(farq)
    farqMassiv = mycursor.fetchone()
    farqSath3=int(str(farqMassiv)[1:(len(farqMassiv)-3)])
    #farqSath = int(str(farqMassiv[(len(farqMassiv) - 1)])[1:len(str(farqMassiv[(len(farqMassiv) - 1)])) - 2])


    mycursor.execute("SELECT reykasathi FROM s_sensor where id=1")
    reyka_height = str(mycursor.fetchone())

    mycursor.execute("SELECT sensorsathi FROM s_sensor where id=1")
    water_height = str(mycursor.fetchone())

    totalHeight = float(reyka_height[1:len(reyka_height) - 2]) + float(water_height[1:len(water_height) - 2])

    if sensr != 0:
        try:
         sensor5b = str(watersensor1.read_register(1, 0, 3))
        except:
            sensorXatoSql5 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valSensorxato5 = (7, 'Sensor ishlamadi')
            mycursor.execute(sensorXatoSql5, valSensorxato5)
            sensor5b=labelIN.cget('text')
            sath1.configure(bg='black',fg="white")

    else:
        sensor5b = '2000'
    sensor5 = round(float(totalHeight) - float(int(sensor5b[0:len(sensor5b) - 1]) / 100), 2)
    labelIN.configure(text=sensor5)

    cub = " Select kub from suvhajmi where sensor_id=1"   ###
    mycursor.execute(cub)
    massiv = mycursor.fetchall()



    sensor5CM = int(sensor5 * 100)+farqSath1
    if sensor5CM < 240:
        kub = float(str(massiv[sensor5CM])[1:len(str(massiv[sensor5CM])) - 2])

        labelINCub.configure(text=kub)
    else:
        labelINCub.configure(text="not found")
    labelINCub.configure(text=kub)
    # Bazaga yozish
    sensorSql5 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi)VALUES (%s,%s,%s,%s)"
    valSensor5 = (1, 1, 1, sensor5)
    mycursor.execute(sensorSql5, valSensor5)
    mydb.commit()
    # sensor6 uchun
    mycursor.execute("SELECT reykasathi FROM s_sensor where id=2")
    reyka_height = str(mycursor.fetchone())

    mycursor.execute("SELECT sensorsathi FROM s_sensor where id=2")
    water_height = str(mycursor.fetchone())
    totalHeight = float(reyka_height[1:len(reyka_height) - 2]) + float(water_height[1:len(water_height) - 2])

    if sensr != 0:
        try:
         sensor6b = str(watersensor2.read_register(1, 0, 3))
        except:
            sensorXatoSql6 = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valSensorxato6 = (8, 'Sensor ishlamadi')
            mycursor.execute(sensorXatoSql6, valSensorxato6)
            sensor6b=labelOut1.cget('text')
            labelOut1.configure(bg='black',fg="white")

    else:
        sensor6b = '2000'

    sensor6 = round(totalHeight - float(int(sensor6b[0:len(sensor6b) - 1]) / 100), 2)
    # #Cubini hisoblash
    cub = " Select kub from suvhajmi where sensor_id=1 "    # jadval berilishi kerak  sensor_id=2
    mycursor.execute(cub)
    massiv = mycursor.fetchall()


    sensor6CM = int(sensor6 * 100)+farqSath2
    if sensor6CM < 240:
        kub = str(massiv[sensor6CM])[1:len(str(massiv[sensor6CM])) - 2]
        labelOut1Cub.configure(text=kub)
    else:
        labelOut1Cub.configure(text="not found")

    labelOut1.configure(text=sensor6)
    sensorSql6 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi)VALUES (%s,%s,%s,%s)"
    valSensor6 = (1, 2, 1, sensor6)
    mycursor.execute(sensorSql6, valSensor6)
    mydb.commit()
    # sensor7 uchun
    mycursor.execute("SELECT reykasathi FROM s_sensor where id=3")
    reyka_height = str(mycursor.fetchone())

    mycursor.execute("SELECT sensorsathi FROM s_sensor where id=3")
    water_height = str(mycursor.fetchone())
    totalHeight = float(reyka_height[1:len(reyka_height) - 2]) + float(water_height[1:len(water_height) - 2])
    if sensr != 0:
        try:
         sensor7b = str(watersensor3.read_register(1, 0, 3))
        except:
            sensorXatoSql = "INSERT INTO xato_sensor(motor_id,status)VALUES (%s,%s)"
            valSensorxato = (7, 'Sensor ishlamadi')
            mycursor.execute(sensorXatoSql, valSensorxato)
            sensor7b=labelOut2.cget('text')
            labelOut2.configure(bg='black',fg="white")
    else:
        sensor7b = '2000'
    sensor7 = round(totalHeight - float(int(sensor7b[0:len(sensor7b) - 1]) / 100), 2)
    cub = " Select kub from suvhajmi where sensor_id=1 "  # jadval berilishi kerak  sensor_id=3


    mycursor.execute(cub)
    massiv = mycursor.fetchall()
    sensor7CM = int(sensor7 * 100)+farqSath3
    if sensor7CM < 240:
        kub = str(massiv[sensor7CM])[1:len(str(massiv[sensor7CM])) - 2]
        labelOut2Cub.configure(text=kub)
    else:
        labelOut2Cub.configure(text="not found")
    labelOut2.configure(text=sensor7)

    sensorSql7 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,suvSathi)VALUES (%s,%s,%s,%s)"
    valSensor7 = (1, 3, 1, sensor7)
    mycursor.execute(sensorSql7, valSensor7)
    mydb.commit()
    labelsensor1.after(5000, water_sensor)

window = Tk()
newWindow=ttk.Notebook(window)
firstWindow=Frame(newWindow,bg="Khaki")
secondWindow=Frame(newWindow)
newWindow.add(secondWindow,text="user")
newWindow.add(firstWindow,text="Settings")

newWindow.pack(expand=True,fill="both")
window.title('SUV INSHOATI NAZORATI')
window.geometry('1200x700')
window.configure(bg="#0099cc")

label = Label(secondWindow,text='Buyruq ', fg='white', bg='black', width=7, font=('italic', 12, 'bold'))

label2b = Label(secondWindow, text= str(buyruq1) , fg='black', bg='white', width=4,
               font=('italic', 16, 'bold'))
label2b.grid(row=1, column=1,columnspan=2 )

label3 = Label(secondWindow, text= str(sana) , fg='black', bg='white', width=16,
               font=('italic', 16, 'bold'))
label3.grid(row=1, column=3 )

label2k = Label(secondWindow, text=' kub ', fg='orange', bg='blue', width=3,
               font=('italic', 14, 'bold'))
label2k.grid(row=1, column=2)
label.grid(row=1,column=1,padx=4)
Label(secondWindow,text='surjina sathi /m').grid(row=2,column=2,padx=1,pady=8)
Label(secondWindow,text='bosilgandagi sathi /m').grid(row=2,column=3,padx=1,pady=8)
Label(secondWindow,text='qanchaga kutarilishi /m').grid(row=2,column=4,padx=1,pady=8)

label1 = Label(secondWindow,text='1', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold'))
label1.grid(row=3, column=1, padx=3,pady=6)

labelsensor1 = Label(secondWindow,font=('Arial', 20), bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
labelsensor1.grid(row=3, column=2)

sath1 = Label(secondWindow,font=('Arial', 20),text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
sath1.grid(row=3, column=3,padx=0)
button11 = Button(secondWindow, width=5, command=on1, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=3, column=5, padx=1, pady=6)
button12 = Button(secondWindow, width=5, command=off1, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=3, column=6, padx=3, pady=6)
button13 = Button(secondWindow, width=5, command=on2, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=3, column=7, padx=1, pady=6)

label2 = Label(secondWindow,text='2', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=4, column=1, padx=1,
                                                                                             pady=6)
labelsensor2 = Label(secondWindow,font=('Arial', 20), bg='white', fg='black', width=5, bd=2,
                     relief=SUNKEN)
labelsensor2.grid(row=4, column=2)
sath2 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath2.grid(row=4, column=3)
button21 = Button(secondWindow, width=5, command=on3, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=4, column=5, padx=1, pady=3)
button22 = Button(secondWindow,width=5, command=off2, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=4, column=6, padx=3, pady=6)
button23 = Button(secondWindow, width=5, command=on4, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=4, column=7, padx=1, pady=6)

label3 = Label(secondWindow,text='3', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=5, column=1, padx=1,
                                                                                             pady=6)
labelsensor3 = Label(secondWindow,font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,
                     relief=SUNKEN)
labelsensor3.grid(row=5, column=2)
sath3 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath3.grid(row=5, column=3)
button31 = Button(secondWindow, width=5, text='tepaga', command=on5, fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=5, column=5, padx=1, pady=6)
button32 = Button(secondWindow, width=5, text='stop', command=off3, fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=5, column=6, padx=1, pady=6)
button33 = Button(secondWindow, width=5, text='pastga', command=on6, fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=5, column=7, padx=1, pady=6)
#
#
# label4 = Label(secondWindow,text='4', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold'))
# label4.grid(row=6, column=1, padx=3,pady=6)
#
# labelsensor4 = Label(secondWindow,font=('Arial', 20), bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
# labelsensor4.grid(row=6, column=2)
#
# sath4 = Label(secondWindow,font=('Arial', 20),text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
# sath4.grid(row=6, column=3,padx=0)
# button41 = Button(secondWindow, width=5, command=on7, text='tepaga', fg='white', bg='green',
#                   font=('italic', 14, 'bold')).grid(row=6, column=5, padx=1, pady=6)
# button42 = Button(secondWindow, width=5, command=off4, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
#     row=6, column=6, padx=3, pady=6)
# button43 = Button(secondWindow, width=5, command=on8, text='pastga', fg='black', bg='yellow',
#                   font=('italic', 14, 'bold')).grid(row=6, column=7, padx=1, pady=6)
#
# label5 = Label(secondWindow,text='5', fg='yellow', bg='blue', width=5, font=('italic', 14, 'bold')).grid(row=7, column=1, padx=1,
#                                                                                              pady=6)
# labelsensor5 = Label(secondWindow,font=('Arial', 20), bg='white', fg='black', width=5, bd=2,
#                      relief=SUNKEN)
# labelsensor5.grid(row=7, column=2)
# sath5 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
#               relief=SUNKEN)
# sath5.grid(row=7, column=3)
# button51 = Button(secondWindow, width=5, command=on9, text='tepaga', fg='white', bg='green',
#                   font=('italic', 14, 'bold')).grid(row=7, column=5, padx=1, pady=3)
# button52 = Button(secondWindow,width=5, command=off5, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
#     row=7, column=6, padx=3, pady=6)
# button53 = Button(secondWindow, width=5, command=on10, text='pastga', fg='black', bg='yellow',
#                   font=('italic', 14, 'bold')).grid(row=7, column=7, padx=1, pady=6)
#
# label6 = Label(secondWindow,text='6', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=8, column=1, padx=1,
#                                                                                              pady=6)
# labelsensor6 = Label(secondWindow,font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,
#                      relief=SUNKEN)
# labelsensor6.grid(row=8, column=2)
# sath6 = Label(secondWindow,font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
#               relief=SUNKEN)
# sath6.grid(row=8, column=3)
# button61 = Button(secondWindow, width=5, text='tepaga', command=on11, fg='white', bg='green',
#                   font=('italic', 14, 'bold')).grid(row=8, column=5, padx=1, pady=6)
# button62 = Button(secondWindow, width=5, text='stop', command=off6, fg='white', bg='red', font=('italic', 14, 'bold')).grid(
#     row=8, column=6, padx=1, pady=6)
# button63 = Button(secondWindow, width=5, text='pastga', command=on12, fg='black', bg='yellow',
#                   font=('italic', 14, 'bold')).grid(row=8, column=7, padx=1, pady=6)
#



inWater=Label(secondWindow,font=('Arial', 16), text='suv sathi', bg='white', fg='blue', width=8, bd=2,
                     relief=SUNKEN)
inWater.grid(row=12, column=2, padx=1, pady=6)
inWaterCub=Label(secondWindow,font=('Arial', 16), text='suv hajmi', bg='white', fg='blue', width=8, bd=2,
                     relief=SUNKEN)
inWaterCub.grid(row=12, column=3, padx=2, pady=6)
labelInZey = Label(secondWindow,text='IN', fg='white', bg='blue', width=7, font=('italic', 16, 'bold')).grid(row=10, column=1,
                                                                                                    padx=1, pady=6)
labelOutPlovon = Label(secondWindow,text='Out1', fg='white', bg='blue', width=7, font=('italic', 16, 'bold')).grid(row=11, column=1,
                                                                                                    padx=1, pady=6)
labelOutPut2 = Label(secondWindow,text='Out2  ', fg='white', bg='blue', width=10, font=('italic', 12, 'bold')).grid(row=12,
                                                                                                               column=1,
                                                                                                               padx=3,
                                                                                                               pady=6)

labelIN = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelIN.grid(row=10, column=2)
labelOut1 = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut1.grid(row=11, column=2)
labelOut1Cub = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut1Cub.grid(row=11, column=3)

labelINCub = Label(secondWindow,text='2', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelINCub.grid(row=10, column=3)
labelOut2Cub = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut2Cub.grid(row=12, column=3)

labelOut2 = Label(secondWindow,text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut2.grid(row=12, column=2)
# buttonOnM = Button(secondWindow,text='onM', command=motor_sensor, fg='white', bg='blue', width=7, font=('italic', 16, 'bold'))
# buttonOnM.grid(row=13, column=1, padx=3, pady=6)
# # buttonOffM=Button(text='offM',fg='white',bg='blue',width=10,font=('italic',12))
# buttonOffM.grid(row=13,column=2,padx=3,pady=6)
#
# buttonOnW = Button(secondWindow,text='onW', command=water_sensor, fg='white', bg='blue', width=7, font=('italic', 16, 'bold'))
# buttonOnW.grid(row=13, column=2, padx=3, pady=6)
# buttonOnCub = Button(secondWindow,text='OnCub', command=water_sensor, fg='white', bg='blue', width=7, font=('italic', 16, 'bold'))
# buttonOnCub.grid(row=13, column=3, padx=3, pady=6)
# buttonOffW=Button(text='offW',fg='white',bg='blue',width=10,font=('italic',12,'bold'))
# buttonOffW.grid(row=13,column=4,padx=3,pady=6)
firstButton=Button(firstWindow,text='registr',bg='#00ffff',width='12',font=('italic', 14, 'bold'))
firstButton.grid(row=1,column=1,padx=55,pady=160)
firstButton2=Button(firstWindow,text='farq',bg='yellow',width='12',font=('italic', 14, 'bold'))
firstButton2.grid(row=1,column=2,padx=35,pady=160)
firstButton3=Button(firstWindow,text='lavozim',bg='#00ffff',width='12',font=('italic', 14, 'bold'))
firstButton3.grid(row=1,column=3,padx=35,pady=160)

firstButton4=Button(firstWindow,text='user',bg='yellow',width='12',font=('italic', 14, 'bold'))
firstButton4.grid(row=1,column=4,padx=35,pady=160)
firstButton5=Button(firstWindow,text='otdel',bg='#00ffff',width='12',font=('italic', 14, 'bold'))
firstButton5.grid(row=1,column=5,padx=35,pady=160)







motor_sensor()
water_sensor()
ogoh()
window.mainloop()


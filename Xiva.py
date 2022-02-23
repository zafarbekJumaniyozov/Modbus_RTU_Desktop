from tkinter import *
import mysql.connector
import time
import serial
import minimalmodbus
from time import sleep
import datetime
import pyautogui
from setuptools import sic

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water')
mycursor = mydb.cursor()
mycursor.execute("SELECT comport FROM s_obekt where indeks='Xiva'")
exCom = str(mycursor.fetchone())
comport = 'COM' + exCom[1:len(exCom) - 2]
global sensr
sensr = 0
global onoff1,onoff2,onoff3,res
res=300
if sensr == 1:
    onoff1 = 0
    onoff2 = 0
    onoff3 = 0
    client1 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client1.serial.baudrate = 9600
    # baudrate
    client1.serial.bytesize = 8
    client1.serial.parity = serial.PARITY_NONE
    client1.serial.stopbits = 1
    client1.serial.timeout = 2  # seconds
    client1.address = 1  # Motor qo'shish  uchun Xiva

    client2 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client2.serial.baudrate = 9600
    # baudrate
    client2.serial.bytesize = 8
    client2.serial.parity = serial.PARITY_NONE
    client2.serial.stopbits = 1
    client2.serial.timeout = 2  # seconds
    client2.address = 4  # Motor datchiklar 4, 3, 2   uchun Xiva

    client3 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client3.serial.baudrate = 9600
    # baudrate
    client3.serial.bytesize = 8
    client3.serial.parity = serial.PARITY_NONE
    client3.serial.stopbits = 1
    client3.serial.timeout = 2  # seconds
    client3.address = 3

    client4 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client4.serial.baudrate = 9600
    # baudrate
    client4.serial.bytesize = 8
    client4.serial.parity = serial.PARITY_NONE
    client4.serial.stopbits = 1
    client4.serial.timeout = 2  # seconds
    client4.address = 2  # input yozilgandan kelgani

    client5 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client5.serial.baudrate = 9600
    # baudrate
    client5.serial.bytesize = 8
    client5.serial.parity = serial.PARITY_NONE
    client5.serial.stopbits = 1
    client5.serial.timeout = 2  # seconds
    client5.address = 5  # sensor 5, 6, 7  uchun Xiva

    client6 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client6.serial.baudrate = 9600
    # baudrate
    client6.serial.bytesize = 8
    client6.serial.parity = serial.PARITY_NONE
    client6.serial.stopbits = 1
    client6.serial.timeout = 2  # seconds
    client6.address = 6

    client7 = minimalmodbus.Instrument(comport, 1)  # port name, slave address (in decimal)
    client7.serial.baudrate = 9600
    # baudrate
    client7.serial.bytesize = 8
    client7.serial.parity = serial.PARITY_NONE
    client7.serial.stopbits = 1
    client7.serial.timeout = 2

    # seconds
    client7.address = 7
else:
    onoff1 = 10 # simulyator
    onoff2 = 10
    onoff3 = 10

# this is the slave address number
# client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
sensor1a = '2000'
sensor2a = '2000'
sensor3a = '2000'
def motor_sensor():
    # past_suv=int(3200)
    global sensor1a,sensor2a,sensor3a,onoff1,res
    if sensr != 0:
        sensor1a = str(client2.read_register(1, 0, 3))
    else:
        if onoff1 == 11:

            if int(sensor1a)- 200 > 2:
                sensor1a = str(int(sensor1a) +res)

        if onoff1 == 12:
            n = str(int(sensor1a) - res)
            sensor1a = n
    pastki_sath1 = 2.35  # bazadan sathni olish kerak vazifa
    print(sensor1a)

    sensor1 = round(pastki_sath1 - float(int(sensor1a[0:len(sensor1a) - 1]) / 100), 2)
    if sensor1 > float(pastki_sath1 - 0.1):
        if sensr != 0:
            onoff1 = 0
            client1.write_register(1, 0x0200)
        else:
            onoff1 = 10

    if sensor1 < 0.1:
        if sensr != 0:
            client1.write_register(2, 0x0200)
            onoff1 = 0
        else:
            onoff1 = 10

    print(onoff1)
    labelsensor1.configure(text=sensor1)

    # Sensor2
    if sensr != 0:
        sensor2a = str(client3.read_register(1, 0, 3))
    else:
        if onoff2 == 11:
            n = str(int(sensor2a)+20)
            sensor2a = n
        if onoff2 == 12:
            n = str(int(sensor2a) - 200)
            sensor2a = n
    pastki_sath2 = 2.31
    sensor2 = round(pastki_sath2 - float(int(sensor2a[0:len(sensor2a) - 1]) / 100), 2)

    labelsensor2.configure(text=sensor2)
    if sensor2>float(pastki_sath2-0.1):
        client1.write_register(3,0x0200)
    if sensor2<0.1:
        client1.write_register(4,0x0200)
    # sensor3

    if sensr != 0:
        sensor3a = str(client4.read_register(1, 0, 3))
    else:
        sensor3a = "2000"
    pastki_sath3 = 2.25
    sensor3 = round(pastki_sath3 - float(int(sensor3a[0:len(sensor3a) - 1]) / 100), 2)
    if sensor3>float(pastki_sath3-0.1):
        client1.write_register(5,0x0200)
    if sensor3<0.1:
        client1.write_register(6,0x0200)
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
def on1(onoff1=12):
    if onoff1 != 11:


        res = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
        if res == None:
            return
        if sensr != 0:
            onoff1 = 1
            client1.write_register(2, 0x0200)
            client1.write_register(1, 0x0100)
        else:
            onoff1 = 11
        sensorSql = "INSERT INTO asos_motor(asos_id,cm,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
        valSensor = (1, 20, onoff1, datetime.datetime.now(), 1, 1)
        mycursor.execute(sensorSql, valSensor)
        mydb.commit()
        labOldsensor1 = float(labelsensor1.cget("text"))
        labelOldsensor1 = Label(window, text=str(labOldsensor1), bg="grey", width=20)
        labelOldsensor1.grid(row=3, column=4)
        sath1.configure(text=str(res))
        onoff1=11
    else:
        pyautogui.alert(text='asdsdsd')
        return


def on2(onoff1=None):
    if onoff1 == 11:
        pyautogui.alert(text='asdsdsd')
        return
    res2 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
    if res2 == None:
        return
    if sensr != 0:
        onoff2 = 1
        client1.write_register(1, 0x0200)
        client1.write_register(2, 0x0100)
    else:
        onoff2 = 11
    sensorSql = "INSERT INTO asos_motor(asos_id,cm,updown,bsana,amal,user_id)VALUES (%s,%s,%s,%s,%s,%s)"
    valSensor = (1, 20, onoff1, datetime.datetime.now(), 1, 1)
    mycursor.execute(sensorSql, valSensor)
    mydb.commit()
    labOldsensor1 = float(labelsensor1.cget("text"))
    labelOldsensor1 = Label(window, text=str(labOldsensor1), bg="grey", width=20)
    labelOldsensor1.grid(row=3, column=4)
    sath1.configure(text=str(res2))


def off1():
    res = pyautogui.confirm(text='', title='1 - motor harakatini to`xtasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    global onoff1
    if sensr != 0:
        client1.write_register(1, 0x0200)
        client1.write_register(2, 0x0200)
        onoff1 = 0
    else:
        onoff1 = 10
    print(onoff1)
def on3():
    res21 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
    if res21 == None:
        return
    if sensr != 0:
        onoff2 = 1
        client1.write_register(4, 0x0200)
        client1.write_register(3, 0x0100)
    else:
        onoff2 = 11
        labOldsensor2 = float(labelsensor2.cget("text"))
        labelOldsensor2 = Label(window, text=str(labOldsensor2), bg="grey", width=20)
        labelOldsensor2.grid(row=4, column=4)
        sath2.configure(text=str(res21))
def on4():
    res22 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
    if res22 == None:
        return
    if sensr != 0:
        onoff2 = 2
        client1.write_register(3, 0x0200)
        client1.write_register(4, 0x0100)
    else:
        onoff2 = 12
        labOldsensor2 = float(labelsensor2.cget("text"))
        labelOldsensor2 = Label(window, text=str(labOldsensor2), bg="grey", width=20)
        labelOldsensor2.grid(row=4, column=4)
        sath2.configure(text=str(res22))
def on5():
    res31 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
    if res31 == None:
        return
    if sensr != 0:
        onoff3 = 1
        client1.write_register(6, 0x0200)
        client1.write_register(5, 0x0100)
        labOldsensor3 = float(labelsensor3.cget("text"))
        labelOldsensor3 = Label(window, text=str(labOldsensor3), bg="grey", width=20)
        labelOldsensor3.grid(row=5, column=4)
        sath3.configure(text=str(res31))
    else:
        onoff3 = 11
        labOldsensor3 = float(labelsensor3.cget("text"))
        labelOldsensor3 = Label(window, text=str(labOldsensor3), bg="grey", width=20)
        labelOldsensor3.grid(row=5, column=4)
        sath3.configure(text=str(res31))
def on6():
    res32 = pyautogui.password(text='Sm da oraliqni kiriting', title='Oraliq masofa', default='', mask='')
    if res32 == None:
        return
    if sensr != 0:
        onoff3 = 2
        client1.write_register(5, 0x0200)
        client1.write_register(6, 0x0100)
        labOldsensor3 = float(labelsensor3.cget("text"))
        labelOldsensor3 = Label(window, text=str(labOldsensor3), bg="grey", width=20)
        labelOldsensor3.grid(row=5, column=4)
        sath3.configure(text=str(res32))
    else:
        onoff3 = 12
        labOldsensor3 = float(labelsensor3.cget("text"))
        labelOldsensor3 = Label(window, text=str(labOldsensor3), bg="grey", width=20)
        labelOldsensor3.grid(row=5, column=4)
        sath3.configure(text=str(res32))

def off2():
    res = pyautogui.confirm(text='', title='1 - motor harakatini to`xtotasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        client1.write_register(3, 0x0200)
        client1.write_register(4, 0x0200)

def off3():
    res = pyautogui.confirm(text='', title='1 - motor harakatini to`xtotasizmi() ?', buttons=['OK', 'Cancel'])
    if res == 'Cancel':
        return
    if sensr != 0:
        client1.write_register(5, 0x0200)
        client1.write_register(6, 0x0200)

def water_sensor():
    mycursor.execute("SELECT reykasathi FROM s_sensor where id=1")
    reyka_height = str(mycursor.fetchone())

    mycursor.execute("SELECT sensorsathi FROM s_sensor where id=1")
    water_height = str(mycursor.fetchone())

    totalHeight = float(reyka_height[1:len(reyka_height) - 2]) + float(water_height[1:len(water_height) - 2])

    if sensr != 0:
        sensor5a = str(client5.read_register(1, 0, 3))
    else:
        sensor5a = '2000'
    sensor5 = round(float(totalHeight) - float(int(sensor5a[0:len(sensor5a) - 1]) / 100), 2)
    labelIN.configure(text=sensor5)

    cub = " Select kub from suvhajmi "
    mycursor.execute(cub)
    massiv = mycursor.fetchall()
    sensor5CM = int(sensor5 * 100)
    if sensor5CM < 240:
        kub = str(massiv[sensor5CM])[1:len(str(massiv[sensor5CM])) - 2]
        labelINCub.configure(text=kub)
    else:
        labelINCub.configure(text="not found")
    labelINCub.configure(text=kub)
    # Bazaga yozish
    sensorSql5 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
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
        sensor6a = str(client6.read_register(1, 0, 3))
    else:
        sensor6a = '2000'

    sensor6 = round(totalHeight - float(int(sensor6a[0:len(sensor6a) - 1]) / 100), 2)
    # #Cubini hisoblash
    cub = " Select kub from suvhajmi "
    mycursor.execute(cub)
    massiv = mycursor.fetchall()
    sensor6CM = int(sensor6 * 100)
    if sensor6CM < 240:
        kub = str(massiv[sensor6CM])[1:len(str(massiv[sensor6CM])) - 2]
        labelOut1Cub.configure(text=kub)
    else:
        labelOut1Cub.configure(text="not found")

    labelOut1.configure(text=sensor6)
    sensorSql6 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
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
        sensor7a = str(client7.read_register(1, 0, 3))
    else:
        sensor7a = '2000'
    sensor7 = round(totalHeight - float(int(sensor7a[0:len(sensor7a) - 1]) / 100), 2)
    cub = " Select kub from suvhajmi "
    mycursor.execute(cub)
    massiv = mycursor.fetchall()
    sensor7CM = int(sensor7 * 100)
    if sensor7CM < 240:
        kub = str(massiv[sensor7CM])[1:len(str(massiv[sensor7CM])) - 2]
        labelOut2Cub.configure(text=kub)
    else:
        labelOut2Cub.configure(text="not found")
    labelOut2.configure(text=sensor7)

    sensorSql7 = "INSERT INTO water_sensor(asos_id,sensor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
    valSensor7 = (1, 3, 1, sensor7)
    mycursor.execute(sensorSql7, valSensor7)
    mydb.commit()
    labelsensor1.after(5000, water_sensor)

window = Tk()
window.title('Polvon kanal')
window.geometry('1200x700')
window.configure(bg="#0099cc")

label = Label(text='SUV INSHOATI NAZORATI', fg='orange', bg='blue', width=20, font=('italic', 25, 'bold'))
label.grid(row=1,column=4,columnspan=3)
Label(text='surjina sathi /m').grid(row=2,column=2,padx=1,pady=8)
Label(text='bosilgandagi sathi /m').grid(row=2,column=3,padx=1,pady=8)
Label(text='qanchaga kutarilishi /m').grid(row=2,column=4,padx=1,pady=8)

label1 = Label(text='1', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold'))
label1.grid(row=3, column=1, padx=3,pady=6)

labelsensor1 = Label(font=('Arial', 20), bg='white', fg='blue', width=5, bd=2,relief=SUNKEN)
labelsensor1.grid(row=3, column=2)

sath1 = Label(font=('Arial', 20),text='', bg='white', fg='blue', width=5, bd=2, relief=SUNKEN)
sath1.grid(row=3, column=3,padx=0)
button11 = Button(window, width=5, command=on1, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=3, column=5, padx=1, pady=6)
button12 = Button(window, width=5, command=off1, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=3, column=6, padx=3, pady=6)
button13 = Button(window, width=5, command=on2, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=3, column=7, padx=1, pady=6)

label2 = Button(text='2', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=4, column=1, padx=1,
                                                                                             pady=6)
labelsensor2 = Label(font=('Arial', 20), bg='white', fg='black', width=5, bd=2,
                     relief=SUNKEN)
labelsensor2.grid(row=4, column=2)
sath2 = Label(font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath2.grid(row=4, column=3)
button21 = Button(window, width=5, command=on3, text='tepaga', fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=4, column=5, padx=1, pady=3)
button22 = Button(window, width=5, command=off2, text='stop', fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=4, column=6, padx=3, pady=6)
button23 = Button(window, width=5, command=on4, text='pastga', fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=4, column=7, padx=1, pady=6)

label3 = Button(text='3', fg='yellow', bg='blue', width=2, font=('italic', 20, 'bold')).grid(row=5, column=1, padx=1,
                                                                                             pady=6)
labelsensor3 = Label(font=('Arial', 20), text=' ', bg='white', fg='blue', width=5, bd=2,
                     relief=SUNKEN)
labelsensor3.grid(row=5, column=2)
sath3 = Label(font=('Arial', 20), text='',bg='white', fg='blue', width=5, bd=2,
              relief=SUNKEN)
sath3.grid(row=5, column=3)
button31 = Button(window, width=5, text='tepaga', command=on5, fg='white', bg='green',
                  font=('italic', 14, 'bold')).grid(row=5, column=5, padx=1, pady=6)
button32 = Button(window, width=5, text='stop', command=off3, fg='white', bg='red', font=('italic', 14, 'bold')).grid(
    row=5, column=6, padx=1, pady=6)
button33 = Button(window, width=5, text='pastga', command=on6, fg='black', bg='yellow',
                  font=('italic', 14, 'bold')).grid(row=5, column=7, padx=1, pady=6)

buttonIn = Button(text='zey-yop', fg='white', bg='blue', width=7, font=('italic', 16, 'bold')).grid(row=10, column=1,
                                                                                                    padx=1, pady=6)
buttonOut = Button(text='polvon', fg='white', bg='blue', width=7, font=('italic', 16, 'bold')).grid(row=11, column=1,
                                                                                                    padx=1, pady=6)
buttonOutPut2 = Button(text='zey pastki  ', fg='white', bg='blue', width=10, font=('italic', 12, 'bold')).grid(row=12,
                                                                                                               column=1,
                                                                                                               padx=3,
                                                                                                               pady=6)

labelIN = Label(text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelIN.grid(row=10, column=2)
labelOut1 = Label(text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut1.grid(row=11, column=2)

labelOut2Cub = Label(text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut2Cub.grid(row=12, column=3)
labelINCub = Label(text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelINCub.grid(row=10, column=3)
labelOut1Cub = Label(text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut1Cub.grid(row=11, column=3)

labelOut2 = Label(text=' ', font=('Arial', 18), bd=2, relief=SUNKEN, bg='white', fg='black', width=8)
labelOut2.grid(row=12, column=2)
buttonOnM = Button(text='onM', command=motor_sensor, fg='white', bg='blue', width=7, font=('italic', 16, 'bold'))
buttonOnM.grid(row=13, column=1, padx=3, pady=6)
# buttonOffM=Button(text='offM',fg='white',bg='blue',width=10,font=('italic',12))
# buttonOffM.grid(row=13,column=2,padx=3,pady=6)

buttonOnW = Button(text='onW', command=water_sensor, fg='white', bg='blue', width=7, font=('italic', 16, 'bold'))
buttonOnW.grid(row=13, column=2, padx=3, pady=6)
buttonOnCub = Button(text='OnCub', command=water_sensor, fg='white', bg='blue', width=7, font=('italic', 16, 'bold'))
buttonOnCub.grid(row=13, column=3, padx=3, pady=6)
# buttonOffW=Button(text='offW',fg='white',bg='blue',width=10,font=('italic',12,'bold'))
# buttonOffW.grid(row=13,column=4,padx=3,pady=6)

motor_sensor()
water_sensor()
window.mainloop()


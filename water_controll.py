from tkinter import *
import mysql.connector
import time
import serial
import minimalmodbus
from time import sleep



client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True
client1.serial.bytesize = 8
client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

client1 = minimalmodbus.Instrument('COM5', 1)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600
# baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  =2      # seconds
client1.address         = 1

# this is the slave address number
#client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='modbus_mysql' )
mycursor=mydb.cursor()


def on1():
    client1.write_register(2, 0x0200)
    client1.write_register(1, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (1,'on')")
    mydb.commit()

def on2():
    client1.write_register(1, 0x0200)
    client1.write_register(2, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (2,'on')")
    mydb.commit()

def on3():
    client1.write_register(4, 0x0200)
    client1.write_register(3, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (3,'on')")
    mydb.commit()

def on4():

    client1.write_register(3, 0x0200)
    client1.write_register(4, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (4,'on')")
    mydb.commit()

def on5():
    client1.write_register(6, 0x0200)
    client1.write_register(5, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (5,'on')")
    mydb.commit()

def on6():
    client1.write_register(5, 0x0200)
    client1.write_register(6, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (6,'on')")
    mydb.commit()


def on7():
    client1.write_register(8, 0x0200)
    client1.write_register(7, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (7,'on')")
    mydb.commit()

def on8():
    client1.write_register(7, 0x0200)
    client1.write_register(8, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (2,'on')")
    mydb.commit()

def on9():
    #client1.write_register(1, 0x0200)#2-modbus
    #client1.write_register(1, 0x0100)#2-modbus
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (3,'on')")
    mydb.commit()

def on10():

    client1.write_register(10, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (4,'on')")
    mydb.commit()

def on11():
    client1.write_register(11, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (5,'on')")
    mydb.commit()

def on12():
    client1.write_register(12, 0x0100)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (6,'on')")
    mydb.commit()


def off1():
    client1.write_register(1, 0x0200)
    client1.write_register(2, 0x0200)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (1,'off')")
    mydb.commit()

def off2():
    client1.write_register(3, 0x0200)
    client1.write_register(4, 0x0200)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (2,'off')")
    mydb.commit()

def off3():
    client1.write_register(5, 0x0200)
    client1.write_register(6, 0x0200)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (3,'off')")
    mydb.commit()
def off4():
    client1.write_register(7, 0x0200)
    client1.write_register(8, 0x0200)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (4,'off')")
    mydb.commit()

def off5():
    client1.write_register(9, 0x0200)
    client1.write_register(10, 0x0200)
    mycursor.execute("INSERT INTO check_motor(motor_number,status) VALUES (5,'off')")
    mydb.commit()


def off6():
    client1.write_register(11, 0x0200)
    client1.write_register(12, 0x0200)
    mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (6,'off')")
    mydb.commit()





window=Tk()
window.title('TOSH SAQA')
window.geometry('1200x700')
window.configure(bg="#0099cc")
window.iconbitmap(r'water_J79_icon.ico')

label=Label(text='Control Motor',fg='orange',bg='blue',width=20,font=('italic',25,'bold')).grid(row=1,column=3,padx=25,pady=6)
labelss=Label(text='Control Motor',fg='orange',bg='blue',width=20,font=('italic',25,'bold')).grid(row=2,column=3)

label1=Label(text='1',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=3,column=1,padx=3,pady=6)

entry1=Entry(font=('Arial',20),bg='white',fg='blue',width=15,bd=2,
            relief=SUNKEN).grid(row=3,column=2)
button11=Button(window,width=5,command=on1,text='Up',fg='white',bg='green',font=('italic',14,'bold')).grid(row=3,column=4,padx=3,pady=6)
button12=Button(window,width=5,command=off1,text='Stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=3,column=5,padx=3,pady=6)
button13=Button(window,width=5,command=on2,text='Down',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=3,column=6,padx=3,pady=6)


label2=Label(text='2',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=4,column=1,padx=3,pady=6)
entry2=Entry(font=('Arial',20),bg='white',fg='black',width=15,bd=2,
            relief=SUNKEN).grid(row=4,column=2)
button21=Button(window,width=5,command=on3,text='Up',fg='white',bg='green',font=('italic',14,'bold')).grid(row=4,column=4,padx=3,pady=6)
button22=Button(window,width=5,command=off2,text='Stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=4,column=5,padx=3,pady=6)
button23=Button(window,width=5,command=on4,text='Down',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=4,column=6,padx=3,pady=6)



label3=Label(text='3',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=5,column=1,padx=3,pady=6)
entry3=Entry(font=('Arial',20),bg='white',fg='blue',width=15,bd=2,
            relief=SUNKEN).grid(row=5,column=2)
button31=Button(window,width=5,text='Up',command=on5,fg='white',bg='green',font=('italic',14,'bold')).grid(row=5,column=4,padx=3,pady=6)
button32=Button(window,width=5,text='Stop',command=off3,fg='white',bg='red',font=('italic',14,'bold')).grid(row=5,column=5,padx=3,pady=6)
button33=Button(window,width=5,text='Down',command=on6,fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=5,column=6,padx=3,pady=6)

label4=Label(text='4',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=6,column=1,padx=3,pady=6)
entry4=Entry(font=('Arial',20),bg='white',fg='blue',width=15,bd=2,
            relief=SUNKEN).grid(row=6,column=2)
button41=Button(window,command=on7,width=5,text='Up',fg='white',bg='green',font=('italic',14,'bold')).grid(row=6,column=4,padx=3,pady=6)
button42=Button(window,command=off4,width=5,text='Stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=6,column=5,padx=3,pady=6)
button43=Button(window,command=on8,width=5,text='Down',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=6,column=6,padx=3,pady=6)


label5=Label(text='5',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=7,column=1,padx=3,pady=6)
entry5=Entry(font=('Arial',20),bg='white',fg='black',width=15,bd=2,
            relief=SUNKEN).grid(row=7,column=2)
button51=Button(window,command=on9,width=5,text='Up',fg='white',bg='green',font=('italic',14,'bold')).grid(row=7,column=4,padx=3,pady=6)
button52=Button(window,command=on5,width=5,text='Stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=7,column=5,padx=3,pady=6)
button53=Button(window,command=on10,width=5,text='Down',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=7,column=6,padx=3,pady=6)



label6=Label(text='6',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=8,column=1,padx=3,pady=6)
entry6=Entry(font=('Arial',20),bg='white',fg='green',width=15,bd=2,
            relief=SUNKEN).grid(row=8,column=2)
button61=Button(window,command=on11,width=5,text='Up',fg='white',bg='green',font=('italic',14,'bold')).grid(row=8,column=4,padx=3,pady=6)
button62=Button(window,command=on6,width=5,text='Stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=8,column=5,padx=3,pady=6)
button63=Button(window,command=on12,width=5,text='Down',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=8,column=6,padx=3,pady=6)

labelInPut=Label(text='InPut',fg='white',bg='blue',width=7,font=('italic',16,'bold')).grid(row=9,column=1,padx=3,pady=6)
labelOutPut=Label(text='OutPut1',fg='white',bg='blue',width=7,font=('italic',16,'bold')).grid(row=9,column=2,padx=3,pady=6)
labelOutPut2=Label(text='OutPut2',fg='white',bg='blue',width=7,font=('italic',16,'bold')).grid(row=9,column=3,padx=3,pady=6)

buttonOfDay = Button(window, width=8, text='OfDay', fg='black', bg='PowderBlue',  font=('italic', 14, 'bold'))\
    .grid(row=3, column=8,padx=15, pady=6)
buttonOfMonth = Button(window, width=8, text='OfMonth', fg='black', bg='PowderBlue', font=('italic', 14, 'bold'))\
    .grid(row=5, column=8, padx=15, pady=6)
buttonOfWeek = Button(window, width=8, text='OfMonth', fg='black', bg='PowderBlue', font=('italic', 14, 'bold'))\
   .grid(row=7, column=8, padx=15, pady=6)
buttonOfYear = Button(window, width=8, text='OfYear', fg='black', bg='PowderBlue', font=('italic', 14, 'bold')).\
   grid(row=9,column=8,padx=15,pady=6)


entryIN=Entry(font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8).grid(row=10,column=1)
entryOut1=Entry(font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8).grid(row=10,column=2)
entryOut2=Entry(font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8).grid(row=10,column=3)
window.mainloop()

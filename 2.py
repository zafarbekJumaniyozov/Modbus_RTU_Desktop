from tkinter import *
import datetime
mylist = ["apple", "banana", "cherry", "melon", "watermelon"]
import mysql.connector

#def printSensors():
   # entry2.insert(1, " g")
def clock():
    a = int(5)
    b = datetime.datetime.now()
    entry2.configure(text=b )
    entry2.after(1000,clock)
def update():
    a=int(5)
window = Tk()
window.geometry("500x300")
window.title("Scale")

entry2 = Label(font=('Arial', 20),text=" ", bg='white', fg='black', width=45, bd=2,
               relief=SUNKEN)


entry2.pack()

clock()

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='modbus_mysql' )
mycursor=mydb.cursor()
s='sdfghjhgf'
def baza():
    sql="INSERT INTO check_motor (motor_number,status) VALUES (%s, %s)"
    val = (1, s)
    mycursor.execute(sql,val)
    mydb.commit()
b=str(3125)
Button(window,command=baza,text='Baza' ).pack()
print(int(b[0:len(b)-1])/100)


window.mainloop()

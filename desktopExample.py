
from tkinter import *
import mysql.connector
import time
import serial
import minimalmodbus
from time import sleep
import datetime

window=Tk()
window.title('Polvon kanal')
window.geometry('1200x700')
window.configure(bg="#0099cc")

label=Label(text='Control Motor',fg='orange',bg='blue',width=20,font=('italic',25,'bold')).grid(row=1,column=3,padx=25,pady=6)

label1=Label(text='1',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=3,column=1,padx=3,pady=6)

labelsensor1=Label(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor1.grid(row=3,column=2)

sath1=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=3,column=3)
button11=Button(window,width=5,text='tepaga',fg='white',bg='green',font=('italic',14,'bold')).grid(row=3,column=4,padx=3,pady=6)
button12=Button(window,width=5,text='stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=3,column=5,padx=3,pady=6)
button13=Button(window,width=5,text='pastga',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=3,column=6,padx=3,pady=6)


label2=Button(text='2',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=4,column=1,padx=3,pady=6)
labelsensor2=Label(font=('Arial',20),bg='white',fg='black',width=5,bd=2,
            relief=SUNKEN)
labelsensor2.grid(row=4,column=2)
sath2=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=4,column=3)
button21=Button(window,width=5,text='tepaga',fg='white',bg='green',font=('italic',14,'bold')).grid(row=4,column=4,padx=3,pady=6)
button22=Button(window,width=5,text='stop',fg='white',bg='red',font=('italic',14,'bold')).grid(row=4,column=5,padx=3,pady=6)
button23=Button(window,width=5,text='pastga',fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=4,column=6,padx=3,pady=6)



label3=Button(text='3',fg='yellow',bg='blue',width=2,font=('italic',20,'bold')).grid(row=5,column=1,padx=3,pady=6)
labelsensor3=Label(font=('Arial',20),text=' ',bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN)
labelsensor3.grid(row=5,column=2)
sath3=Entry(font=('Arial',20),bg='white',fg='blue',width=5,bd=2,
            relief=SUNKEN).grid(row=5,column=3)
button31=Button(window,width=5,text='tepaga',fg='white',bg='green',font=('italic',14,'bold')).grid(row=5,column=4,padx=3,pady=6)
button32=Button(window,width=5,text='stop',command=off3,fg='white',bg='red',font=('italic',14,'bold')).grid(row=5,column=5,padx=3,pady=6)
button33=Button(window,width=5,text='pastga',command=on6,fg='black',bg='yellow',font=('italic',14,'bold')).grid(row=5,column=6,padx=3,pady=6)


buttonIn=Button(text='zey-yop',fg='white',bg='blue',width=7,font=('italic',16,'bold')).grid(row=10,column=1,padx=3,pady=6)
buttonOut=Button(text='polvon',fg='white',bg='blue',width=7,font=('italic',16,'bold')).grid(row=11,column=1,padx=3,pady=6)
buttonOutPut2=Button(text='zey pastki  ',fg='white',bg='blue',width=10,font=('italic',12,'bold')).grid(row=12,column=1,padx=3,pady=6)



labelIN=Label(text=' ',font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8)
labelIN.grid(row=10,column=2)
labelOut1=Label(text=' ',font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8)
labelOut1.grid(row=11,column=2)

labelOut2=Label(text=' ',font=('Arial',18),bd=2, relief=SUNKEN,bg='white',fg='black',width=8)
labelOut2.grid(row=12,column=2)
buttonOnM=Button(text='onM',command=motor_sensor,fg='white',bg='blue',width=7,font=('italic',16,'bold'))
buttonOnM.grid(row=13,column=1,padx=3,pady=6)
buttonOffM=Button(text='offM',fg='white',bg='blue',width=10,font=('italic',12,'bold'))
buttonOffM.grid(row=13,column=2,padx=3,pady=6)

buttonOnW=Button(text='onW',command=water_sensor,fg='white',bg='blue',width=7,font=('italic',16,'bold'))
buttonOnW.grid(row=13,column=3,padx=3,pady=6)
buttonOffW=Button(text='offW',fg='white',bg='blue',width=10,font=('italic',12,'bold'))
buttonOffW.grid(row=13,column=4,padx=3,pady=6)


window.mainloop()

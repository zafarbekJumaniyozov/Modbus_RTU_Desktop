from tkinter import *

#def submit():
 #   print("A"+str(scale.get()))
def printSensors():
    entry2.insert(mylist[1])

window=Tk()
window.geometry("400x300")
window.title("Scale")
#scale=Scale(window,from_=100,to=0)
#scale.pack()

entry2=Entry(font=('Arial',20),bg='white',fg='black',width=15,bd=2,
            relief=SUNKEN)
mylist = ["apple", "banana", "cherry","melon","watermelon"]

entry2.pack()
#button=Button(window,command=submit,text="submit")
#button.pack()
for i in  mylist:
    print(i+" ")


def printSensor2():
    # client1.write_register(2, 0x0200)
    # mycursor.execute("INSERT INTO check_motor(motor_number,status)VALUES (1,'off')")
    # mydb.commit()
    labels1.insert("client2.read_register(1, 0, 3)")


labels1=Label(font=('Arial',20),bg='white',fg='blue',width=15,bd=2,
            relief=SUNKEN)
labels1.pack()

window.mainloop()

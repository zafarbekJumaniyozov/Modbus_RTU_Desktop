from tkinter import *
import mysql.connector
import json,requests
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water')
mycursor = mydb.cursor()
# import requests
#
# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}
#
# x = requests.post(url, data = myobj)
#
# print(x.text)
def refresh():
    sql="Select * from s_motor "
    mycursor.execute(sql)
    refresh2=mycursor.fetchall()
    employee = []
    content = {}
    for result in refresh2:
        content = {'max': result[4], 'min': result[3],}
        employee.append(content)

    print(employee)
    print(json.dumps(content))
    r=requests.get(url="",)



window=Tk()
window.geometry("400x200")
window.configure(bg="yellow")
refresh=Button(window,text="refresh",command=refresh,bg="white",width='12',font=('italic', 14, 'bold'))
refresh.grid(row=1,column=1,pady=50,padx=100)
window.mainloop()

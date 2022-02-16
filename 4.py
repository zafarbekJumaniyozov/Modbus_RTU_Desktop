import threading

# import the time module
import time
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    username='info!traffic',
    password='masterkalit',
    database='water' )
mycursor=mydb.cursor()


# define the countdown func.
def countdown():
    b=True
    while b!=False:

        time.sleep(5)

    #sensor1a=str(client2.read_register(1,0,3))
    #pastki_sath1 = 2.35#bazadan sathni olish kerak vazifa
        sensor1=44.5
        #pastki_sath1-float(int(sensor1a[0:len(sensor1a)-1])/100)
    #labelsensor1.configure(text=str(sensor1) )

        sensorSql1 = "INSERT INTO motor_sensor(asos_id,motor_id,user_id,cm)VALUES (%s,%s,%s,%s)"
        valSensor1 = (1, 2, 1, sensor1)
        mycursor.execute(sensorSql1, valSensor1)
        mydb.commit()
        print('Fire in the hole!!')



# function call
countdown()
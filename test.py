import serial
import minimalmodbus
client4 = minimalmodbus.Instrument('Com5', 1)  # port name, slave address (in decimal)
client4.serial.baudrate = 9600
# baudrate
client4.serial.bytesize = 8
client4.serial.parity = serial.PARITY_NONE
client4.serial.stopbits = 1
client4.serial.timeout = 2  # seconds
client4.address = 2  # input yozi
sensor3a = str(client4.read_register(1, 0, 3))
print(sensor3a)
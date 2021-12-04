import serial

arduinoSensorProx = serial.Serial("COM4",9600)
arduinoJuez2 = serial.Serial("COM5",9600)

def getDistancia():
    return float(arduinoSensorProx.readline())

def getJuez2():
    return arduinoJuez2.readline().decode('ascii').strip()
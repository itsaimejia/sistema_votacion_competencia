import serial

arduinoSensorProx = serial.Serial("COM4",9600)
#arduinoJuez1 = serial.Serial("COM5",9600)
arduinoJuez2 = serial.Serial("COM5",9600)
#arduinoJuez3 = serial.Serial("COM5",9600)

def getDistancia():
    return float(arduinoSensorProx.readline())

# def getJuez1():
#     return arduinoJuez1.readline().decode('ascii').strip()

def getJuez2():
    return arduinoJuez2.readline().decode('ascii').strip()

# def getJuez3():
#     return arduinoJuez3.readline().decode('ascii').strip()
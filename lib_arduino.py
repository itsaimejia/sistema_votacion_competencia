import serial, time

ard = serial.Serial("COM5",9600)

def getDistancia():
    return float(ard.readline())
        
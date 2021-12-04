import time
from tkinter import *
from tkinter import PhotoImage
import tkinter
import pygame
import threading as tr
import serial
pygame.mixer.init()

arduinoSensorProx = serial.Serial("COM4",9600)
arduinoJuez2 = serial.Serial("COM5",9600)

#variables globales
isRun = True
listaDistancias = []


#configuracion ventana aplicacion
root = Tk()
root.attributes("-fullscreen",True) 
root.title("Sistema de Conteo")
root.config(bg="black")
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)

#imagenes 
imgLuzVerde = tkinter.PhotoImage(file='verde.png')
imgLuzRoja = tkinter.PhotoImage(file='rojo.png')
imgLuzBlanca = tkinter.PhotoImage(file='blanco.png')
imgLuzNegra=tkinter.PhotoImage(file='negro.png')

#labels

#label tiempo (titulo y valor)
Label(root,text="Tiempo",font="digital-7 90",fg="red",bg="black").grid(row=0, column=1, sticky='NSEW')
lblTiempo=tkinter.Label(root,text="60",font="digital-7 130",fg="green",bg="black")
lblTiempo.grid(row=1, column=1, sticky='NSEW')

#label distancia (titulo y valor)
Label(root,text="Distancia", font="digital-7 45",fg="yellow",bg="black").grid(row=0, column=2, sticky='NSEW')
lblDistancia=tkinter.Label(root,text="0.0",font="digital-7 65",fg="blue",bg="black")
lblDistancia.grid(row=1, column=2, sticky='NSEW')

#definicion de label jueces
lblJuez1=Label(root,image=imgLuzNegra,bg="black")
lblJuez1.grid(row=2, column=0, sticky='NSEW')
lblJuez2=Label(root,image=imgLuzNegra,bg="black")
lblJuez2.grid(row=2, column=1, sticky='NSEW')
lblJuez3=Label(root,image=imgLuzNegra,bg="black")
lblJuez3.grid(row=2, column=2, sticky='NSEW')

def resetPantalla():
    lblJuez1.config(image=imgLuzNegra,bg="black")
    lblJuez2.config(image=imgLuzNegra,bg="black")
    lblJuez3.config(image=imgLuzNegra,bg="black")
    cronometro()
    
    
#actualizar semaforo a todos verde
def lucesVerdes():
    lblJuez1.config(image=imgLuzVerde,bg="black")
    lblJuez2.config(image=imgLuzVerde,bg="black")
    lblJuez3.config(image=imgLuzVerde,bg="black")

#conseguir lista de distancias
def getDistancia():
    aux = []
    while isRun:
        aux.append(float(arduinoSensorProx.readline().decode('ascii').strip()))
    
    global listaDistancias
    listaDistancias = aux

#actualizar label distancia (valor)
def updateDistancia():
    var = min(listaDistancias)
    lblDistancia.configure(text=("{0}".format(round(var,1))))
    
def cronometro():
    temp = 5
    while temp >= 0:
        lblTiempo.configure(text=("{0}".format(temp)))
        root.update()
        temp -= 1
        time.sleep(1)
        if temp == 0:
            global isRun
            isRun = False
            hiloSensorProx.join()
            updateDistancia()
            lucesVerdes()
            
#definicion hilos

#hilo para el sensor de proximidad
hiloSensorProx = tr.Thread(target=getDistancia)
hiloSensorProx.start() 

 
    
    # pygame.mixer.music.load("chicharra-2-.mp3")
    # pygame.mixer.music.play(loops=1)
          
btn = Button(root, text='Iniciar cuenta Regresiva', bd='5',
             command= cronometro,font="times 14 bold",fg="white",bg="black",borderwidth=0).grid(row=4, column=0, columnspan=3, sticky='NSEW')

root.mainloop()
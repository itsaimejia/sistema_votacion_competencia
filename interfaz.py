import time
from tkinter import *
from tkinter import PhotoImage
import tkinter
import pygame
import threading as tr
import LibArduino as lard

pygame.mixer.init()

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
    lblDistancia.configure(text="0.0")
    cronometro()
    
    
#actualizar semaforo a todos verde
def lucesVerdes():
    lblJuez1.config(image=imgLuzVerde,bg="black")
    lblJuez2.config(image=imgLuzVerde,bg="black")
    lblJuez3.config(image=imgLuzVerde,bg="black")



#actualizar label distancia (valor)
def updateDistancia(listaDistancias):
    var = min(listaDistancias)
    lblDistancia.configure(text=("{0}".format(var)))
    
def desicionesJueces():
    desJuez1 = lard.getJuez1()
    desJuez2 = lard.getJuez2()
    desJuez3 = lard.getJuez3()
    
    contadorDes = 0
    if(desJuez1 == "ROJOJUEZ1"):
        lblJuez1.config(image=imgLuzRoja,bg="black")
    if(desJuez1 == "BLANCOJUEZ1"):
        lblJuez1.config(image=imgLuzBlanca,bg="black")
        contadorDes += 1
    
    if(desJuez2 == "ROJOJUEZ2"):
        lblJuez2.config(image=imgLuzRoja,bg="black")
    if(desJuez2 == "BLANCOJUEZ2"):
        lblJuez2.config(image=imgLuzBlanca,bg="black")
        contadorDes += 1
            
    if(desJuez3 == "ROJOJUEZ3"):
        lblJuez3.config(image=imgLuzRoja,bg="black")
    if(desJuez3 == "BLANCOJUEZ3"):
        lblJuez3.config(image=imgLuzBlanca,bg="black")
        contadorDes += 1

def cronometro():
    tiempoCronometro = 10
    listaDistancias = []
    while tiempoCronometro >= 0:
        lblTiempo.configure(text=("{0}".format(tiempoCronometro)))
        root.update()
        
        listaDistancias.append(lard.getDistancia()) #conseguir lista de distancias
        
        tiempoCronometro -= 1
        time.sleep(1)
        if tiempoCronometro == 0:
            updateDistancia(listaDistancias)
            lucesVerdes()
            
            
#definicion hilos

#hilo para el sensor de proximidad
# hiloSensorProx = tr.Thread(target=getDistancia)
# hiloSensorProx.start() 
hiloVotacion = tr.Thread(target=desicionesJueces)
hiloVotacion.start()

 
    
# pygame.mixer.music.load("chicharra-2-.mp3")
# pygame.mixer.music.play(loops=1)

#boton para desencadenar pruebas (se borrara)
btn = Button(root, text='Iniciar cuenta Regresiva', bd='5',
             command= resetPantalla,font="times 14 bold",fg="white",bg="black",borderwidth=0).grid(row=4, column=0, columnspan=3, sticky='NSEW')

root.mainloop()
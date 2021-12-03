import time
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
import tkinter
import lib_arduino as lard
import pygame

pygame.mixer.init()

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
luz_verde = tkinter.PhotoImage(file='verde.png')
luz_rojo = tkinter.PhotoImage(file='rojo.png')
luz_blanco = tkinter.PhotoImage(file='blanco.png')
fondo_negro=tkinter.PhotoImage(file='negro.png')


Label(root,text="Tiempo",font="digital-7 90",fg="red",bg="black").grid(row=0, column=1, sticky='NSEW')
lblTiempo=tkinter.Label(root,text="60",font="digital-7 130",fg="green",bg="black")
lblTiempo.grid(row=1, column=1, sticky='NSEW')

Label(root,text="Distancia", font="digital-7 45",fg="yellow",bg="black").grid(row=0, column=2, sticky='NSEW')
lblDistancia=tkinter.Label(root,text="0.0",font="digital-7 65",fg="blue",bg="black")
lblDistancia.grid(row=1, column=2, sticky='NSEW')

lblJuez1=Label(root,image=fondo_negro,bg="black")
lblJuez1.grid(row=2, column=0, sticky='NSEW')
lblJuez2=Label(root,image=fondo_negro,bg="black")
lblJuez2.grid(row=2, column=1, sticky='NSEW')
lblJuez3=Label(root,image=fondo_negro,bg="black")
lblJuez3.grid(row=2, column=2, sticky='NSEW')

def actualizarLuces():
    lblJuez1.config(image=luz_rojo,bg="black")
    lblJuez2.config(image=luz_blanco,bg="black")
    lblJuez3.config(image=luz_blanco,bg="black")

def updateDistancia(lista):
    var = min(lista)
    lblDistancia.configure(text=("{0}".format(round(var,1))))

def submit():
    temp = 60
    listaDistancias = []
    while temp >= 0:
        
        
        lblTiempo.configure(text=("{0}".format(temp)))
        root.update()
        temp -= 1
        listaDistancias.append(lard.getDistancia())
        time.sleep(1)
        if temp == 0:
            print(listaDistancias)
            updateDistancia(listaDistancias)
            actualizarLuces()
        
    
    # pygame.mixer.music.load("chicharra-2-.mp3")
    # pygame.mixer.music.play(loops=1)
          
btn = Button(root, text='Iniciar cuenta Regresiva', bd='5',
             command= submit,font="times 14 bold",fg="white",bg="black",borderwidth=0).grid(row=4, column=0, columnspan=3, sticky='NSEW')

root.mainloop()
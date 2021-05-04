#HECHO POR RIVERA GARCIA JONATAHN 4IV9
from peso import *
from velocidad import *
from colores import *
from altura import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import re
from io import open

class FramePrincipal:
    def __init__(self, master):
            self.master = master
            master.title("EXAMEN XD")
            master.config(bg="purple")
            master.geometry('500x500')
            #el titulo y su estilo
            self.titulo = Label()
            self.titulo.pack(anchor = CENTER)
            self.titulo.config(text="GRAFICAS", fg = "white", bg = "purple")
            #el css de las instrucciones y pues rosita todo por que se ve bonitoo
            self.ins = Label()
            self.ins.pack(anchor = CENTER)
                                                
            self.reg = Button(self.master, text="PESO", command= self.peso)
            self.reg.place(x=120, y = 110, width= 180, height=40)
            self.reg.config(fg = "white", bg="deep pink", font = ("Arial", 15),)

            self.rag = Button(self.master, text="ALTURA", command= self.altura)
            self.rag.place(x=120, y = 220, width= 180, height=40)
            self.rag.config(fg = "white",bg="deep pink", font = ("Arial", 15),)

            self.rig = Button(self.master, text="VELOCIDAD", command= self.velocidad)
            self.rig.place(x=120, y = 330, width= 180, height=40)
            self.rig.config(fg = "white",bg="deep pink", font = ("Arial", 15),)

            self.rog = Button(self.master, text="COLORES", command= self.colores)
            self.rog.place(x=120, y = 440, width= 180, height=40)
            self.rog.config(fg = "white",bg="deep pink", font = ("Arial", 15),)
            
        
        
    def peso(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'purple')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Graficas",bg='purple', fg = "white")
        self.PESOB = Button(new_window, text = "Barra", command = self.barra)
        self.PESOB.place(x = 100, y =80, width = 280, height = 30)
        self.PESOB.config(fg = 'white',bg='purple')
        
        self.PESOP = Button(new_window, text = "Pastel", command = self.pastel)
        self.PESOP.place(x = 100, y =130, width = 280, height = 30)
        self.PESOP.config(fg = 'white',bg='purple')
        
        self.PESOF = Button(new_window, text = "Frecuencia Abs", command = self.abs)
        self.PESOF.place(x = 100, y =180, width = 280, height = 30)
        self.PESOF.config(fg = 'white',bg='purple')
        
        self.PESOPO = Button(new_window, text = "Poligono", command = self.poo)
        self.PESOPO.place(x = 100, y =230, width = 280, height = 30)
        self.PESOPO.config(fg = 'white',bg='purple')
        


    def barra(self):
        pbarra()
        
    def pastel(self):
        ppastel()
        
    def abs(self):
        pFAcumulada()
        
    def poo(self):
        pesoPoligonos()

    
        
        
    def altura(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Graficas",bg='purple', fg = "white")
        self.VENTANA = Button(new_window, text = "Barra", command = self.barra2)
        self.VENTANA.place(x = 100, y =80, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Pastel", command = self.pastel2)
        self.VENTANA.place(x = 100, y =130, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Frecuencia Abs", command = self.abs2)
        self.VENTANA.place(x = 100, y =180, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Poligono", command = self.poo2)
        self.VENTANA.place(x = 100, y =230, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')


    def barra2(self):
        abarra()
        
    def pastel2(self):
        apastel()
        
    def abs2(self):
        aFAcumulada()
        
    def poo2(self):
        aPoligonos()

        
        
    def velocidad(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Eliga la grafica",bg='purple', fg = "white")
        self.VENTANA = Button(new_window, text = "Barra", command = self.barra3)
        self.VENTANA.place(x = 100, y =80, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Pastel", command = self.pastel3)
        self.VENTANA.place(x = 100, y =130, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Frecuencia Abs", command = self.abs3)
        self.VENTANA.place(x = 100, y =180, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Poligono", command = self.poo3)
        self.VENTANA.place(x = 100, y =230, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')


    def barra3(self):
        vbarra()
        
    def pastel3(self):
        vPastel()
        
    def abs3(self):
        vFAcumulada()
        
    def poo3(self):
        vPoligono()
        
        

    def colores(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Eliga la grafica",bg='purple', fg = "white")
        self.VENTANA = Button(new_window, text = "Barra", command = self.barra4)
        self.VENTANA.place(x = 100, y =80, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Pastel", command = self.pastel4)
        self.VENTANA.place(x = 100, y =130, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Frecuencia Abs", command = self.abs4)
        self.VENTANA.place(x = 100, y =180, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')
        
        self.VENTANA = Button(new_window, text = "Poligono", command = self.poo4)
        self.VENTANA.place(x = 100, y =230, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='purple')


    def barra4(self):
        cbarra()
        
    def pastel4(self):
        cpastel()
        
    def abs4(self):
        cFAcumulada()
        
    def poo4(self):
        cPoligonos() 
        
    
                               
                                                           
root = Tk()
root.resizable(False, False)
miVentana =FramePrincipal(root)
root.mainloop()

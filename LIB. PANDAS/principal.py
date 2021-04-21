from tkinter import *
import pandas as pd
pd.__version__

camaras = pd.read_csv("csv_camaras_2.csv")


def consultas():
    
   
    ventana = Tk()
    ventana.title("PROGRAMA DE CONSULTAS")
    ventana.geometry("250x200")
    ventana.config(bg="purple")
    btnIniciar1 = Button(ventana, text="CONSULTA 1", command = consulta1).place(x=20, y=10)
    btnIniciar2 = Button(ventana, text="CONSULTA 2", command = consulta2).place(x=20, y=50)
    btnIniciar3 = Button(ventana, text="CONSULTA 3", command = consulta3).place(x=20, y=90)
    btnIniciar4 = Button(ventana, text="CONSULTA 4").place(x=20, y=130)
    btnIniciar5 = Button(ventana, text="CONSULTA 5").place(x=20, y=170)
    btnIniciar6 = Button(ventana, text="CONSULTA 6").place(x=150, y=10)
    btnIniciar7 = Button(ventana, text="CONSULTA 7").place(x=150, y=50)
    btnIniciar8 = Button(ventana, text="CONSULTA 8").place(x=150, y=90)
    btnIniciar9 = Button(ventana, text="CONSULTA 9").place(x=150, y=130)
    btnIniciar10 = Button(ventana, text="CONSULTA 10").place(x=150, y=170)
    
    

def consulta1 ():
    consulta11 = Tk()
    consulta11.title("Consulta 1")
    consulta11.geometry("300x410")
    label1= Label(consulta11, text = camaras.loc[camaras['Zoom tele (T)'] == 140,['Model','Price']]).place(x=0, y =0)

def consulta2():
    consulta22 = Tk()
    consulta22.title("Consulta 2")
    consulta22.geometry("300x410")
    label1= Label(consulta22, text = camaras.loc[camaras['Normal focus range'] < 50,['Model','Dimensions', 'Price']]).place(x=0, y =0)
    
def consulta3():
    consulta33 = Tk()
    consulta33.title("Consulta 3")
    consulta33.geometry("300x410")
    label1= Label(consulta33, text = camaras.loc[camaras['Model'].str.endswith("A10")]).place(x=0, y =0)
    

    
    
principal = Tk()
principal.title("PAGINA PRINCIPAL")
principal.geometry("300x300")
principal.config(bg="purple")
btnIniciar = Button(principal, text="INICIAR POGRAMA", command = consultas).place(x=100, y=130)
principal.mainloop()





   
 





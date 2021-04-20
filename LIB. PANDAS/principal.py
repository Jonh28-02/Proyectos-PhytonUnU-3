from tkinter import *
import pandas as pd
pd.__version__

camaras = pd.read_csv("csv_camaras_2.csv")
camaras.set_index("Model", inplace=True)

def consultas():
    
   
    ventana = Tk()
    ventana.title("PROGRAMA DE CONSULTAS")
    ventana.geometry("250x200")
    ventana.config(bg="purple")
    btnIniciar = Button(ventana, text="CONSULTA 1").place(x=20, y=10)
    btnIniciar = Button(ventana, text="CONSULTA 2").place(x=20, y=50)
    btnIniciar = Button(ventana, text="CONSULTA 3").place(x=20, y=90)
    btnIniciar = Button(ventana, text="CONSULTA 4").place(x=20, y=130)
    btnIniciar = Button(ventana, text="CONSULTA 5").place(x=20, y=170)
    btnIniciar = Button(ventana, text="CONSULTA 6").place(x=150, y=10)
    btnIniciar = Button(ventana, text="CONSULTA 7").place(x=150, y=50)
    btnIniciar = Button(ventana, text="CONSULTA 8").place(x=150, y=90)
    btnIniciar = Button(ventana, text="CONSULTA 9").place(x=150, y=130)
    btnIniciar = Button(ventana, text="CONSULTA 10").place(x=150, y=170)
    
    

def consulta1 ():
    print("hola")
    

    
    
principal = Tk()
principal.title("PAGINA PRINCIPAL")
principal.geometry("300x300")
principal.config(bg="purple")
btnIniciar = Button(principal, text="INICIAR POGRAMA", command = consultas).place(x=100, y=130)
principal.mainloop()
print(camaras.loc[camaras['Zoom tele (T)'] == 140,['Price']])




   
 





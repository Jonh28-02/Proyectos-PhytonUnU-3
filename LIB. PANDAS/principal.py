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
    btnIniciar4 = Button(ventana, text="CONSULTA 4", command = consulta4).place(x=20, y=130)
    btnIniciar5 = Button(ventana, text="CONSULTA 5", command = consulta5).place(x=20, y=170)
    btnIniciar6 = Button(ventana, text="CONSULTA 6", command = consulta6).place(x=150, y=10)
    btnIniciar7 = Button(ventana, text="CONSULTA 7", command = consulta7).place(x=150, y=50)
    btnIniciar8 = Button(ventana, text="CONSULTA 8", command = consulta8).place(x=150, y=90)
    btnIniciar9 = Button(ventana, text="CONSULTA 9", command = consulta9).place(x=150, y=130)
    btnIniciar10 = Button(ventana, text="CONSULTA 10", command = consulta10).place(x=150, y=170)
    
    

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
    
def consulta4():
    consulta44 = Tk()
    consulta44.title("Consulta 4")
    consulta44.geometry("350x410")
    label1= Label(consulta44, text = camaras.loc[camaras['Model'].str.startswith("Canon")&(camaras['Storage included']==8)]).place(x=0, y =0)
    
def consulta5():
    consulta55 = Tk()
    consulta55.title("Consulta 5")
    consulta55.geometry("300x410")
    label1= Label(consulta55, text = camaras.loc[camaras['Model'].str.startswith("Casio") & (camaras['Price'] < 250) & (camaras['Weight (inc. batteries)'] <240)]).place(x=0, y =0)

def consulta6():
    consulta66 = Tk()
    consulta66.title("Consulta 6")
    consulta66.geometry("300x410")
    label1= Label(consulta66, text = camaras.loc[camaras['Model'].str.startswith("Fujifilm") & (camaras['Macro focus range'] == 8) & (camaras['Normal focus range'] > 50) & (camaras['Storage included'] > 10)]).place(x=0, y =0)                   

def consulta7():
    consulta77 = Tk()
    consulta77.title("Consulta 7")
    consulta77.geometry("350x410")
    label1= Label(consulta77, text = camaras.loc[camaras['Price'] > 1000 & (camaras['Weight (inc. batteries)']>1000), ['Model', 'Price']]).place(x=0, y =0)
    
def consulta8():
    consulta88 = Tk()
    consulta88.title("Consulta 8")
    consulta88.geometry("350x410")
    label1= Label(consulta88, text = camaras.loc[camaras['Model'].str.startswith("Sony")&(camaras['Zoom tele (T)']==114),('Model','Zoom tele (T)','Price')]).place(x=0, y =0)

def consulta9():
    consulta99 = Tk()
    consulta99.title("Consulta 9")
    consulta99.geometry("300x410")
    label1= Label(consulta99, text = camaras.loc[camaras['Model'].str.startswith("Pentax")&(camaras['Zoom tele (T)']==114)&(camaras['Normal focus range']==4)&(camaras['Macro focus range']==5)&(camaras['Storage included']==16)]).place(x=0, y =0)

def consulta10():
    consulta100 = Tk()
    consulta100.title("Consulta 10")
    consulta100.geometry("350x410")
    label1= Label(consulta100, text = camaras.loc[camaras['Model'].str.startswith("Nikon")&(camaras['Zoom tele (T)']==114)&(camaras['Normal focus range']==30)&(camaras['Macro focus range']==4)&(camaras['Storage included']==13)&(camaras['Weight (inc. batteries)']==175)&(camaras['Dimensions']==93)&(camaras['Price']==279),['Model','Zoom tele (T)','Price']]).place(x=0, y =0)
    




 





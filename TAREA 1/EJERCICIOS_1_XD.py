menu="""
Bienvenido al Programa xd
MENU

1. Ejercicio 1
2. Ejercicio 2
3. Ejercicio 3
4. Ejercicio 4
5. Ejercicio 5
6. Ejercicio 6
7. Ejercicio 7
8. Ejercicio 8
9. Ejercicio 9
10. Ejercicio 10
11. Salir
"""
def Ejercicio_1():
     sueldo=int(input("Ingresa tu salario"))
     if sueldo < 4000:
         print((sueldo * .15)+sueldo)
     else:
         print((sueldo * .08)+sueldo)
         

def Ejercicio_2():
     edad=int(input("Ingresa tu edad"))
     if edad < 10:
          print("Tu monto a pagar es de: "(50*.75), "soles")
     else:
          print("Tu monto a pagar es de 50 soles")


def Ejercicio_3():
  print("xd")

def Ejercicio_4():
  print("xd")

def Ejercicio_5():
  print("xd")

def Ejercicio_6():
  print("xd")

def Ejercicio_7():

  print("xd")
def Ejercicio_8():
  print("xd")

def Ejercicio_9():
  print("xd")

def Ejercicio_10():
  print("xd")

while True:

     print(menu)
     op=int(input("Ingrese la opcion que desee xd:"))

     if op is 1:
          Ejercicio_1()
     elif op is 2:
          Ejercicio_2()
     elif op is 3:
          Ejercicio_3()
     elif op is 4:
          Ejercicio_4()
     elif op is 5:
          Ejercicio_5()
     elif op is 6:
          Ejercicio_6()
     elif op is 7:
          Ejercicio_7()
     elif op is 8:
          Ejercicio_8()
     elif op is 9:
          Ejercicio_9()
     elif op is 10:
          Ejercicio_10()
     elif op is 11:
          break
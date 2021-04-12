
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
     mes=int(input("Ingresa el numero de mes "))
     monto=int(input("Ingrese el monto "))

     if mes < 2 or mes > 2:
          print("Tu monto a pagar es de: ", monto)
     else:
          print("Tu monto a pagar es de: ", monto * .75)


def Ejercicio_4():
     num=int(input("Ingresa un numero"))
     while num >= 10:
      num=int(input("Ingresa un numero"))
     if num < 10:
          print("El numero es: ", num)
               

def Ejercicio_5():
     num=int(input("Ingresa un numero"))
     while num <= 0 or num >= 20:
      num=int(input("Ingresa un numero"))
     if num > 0 and num < 20:
        print("El numero es: ", num)
     

def Ejercicio_6():
     num=int(input("Ingresa un numero: "))
     nv=1
     while num <= 0 or num >= 20:
      num=int(input("Ingresa un numero: "))
      nv = nv+1
     if num > 0 and num < 20:
        print("El numero es: ", num)
     print("Ingresaste el numero ",nv , " veces")
     
def Ejercicio_7():

     suma = 0
     numero = int(input("Ingrese un número: "))
     while numero>0:
       suma = (numero*(numero+1))/2
       break
     print ("La suma total es de :",suma)


def Ejercicio_9():
     suma = 0
     while suma < 100:
          num = int(input("Ingrese un numero: "))
          suma = suma + num
     print("La suma es de: ", suma)  

def Ejercicio_8():
     suma = 0
     print("Si deseas detener la suma ingresa 0")
     num = int(input("Ingrese un numero para confirmar lo entendido: "))
     while num < 0 or num > 0:
          num = int(input("Ingrese un numero: "))
          suma = suma + num
     # print("La suma es de: ", suma)

def Ejercicio_10():
     nombre=input("Ingresa tu nombre: ")
     NH=int(input("Ingresa el numero de hijos: "))
     HT=int(input("Ingresa las horas trabajadas: "))
     HE=int(input("Ingresa las horas extra trabajadas: "))
     PH=int(input("Ingresa el pago por hora: "))

     print("El trabajador ",nombre)
     print("Tiene un monto de horas normales igual a: ",HT*PH,"un monto por horas extra de: ",HE*(PH*1.5),"y una bonificacion de: ", NH*.5)
     print("El pago total sera de: ", ((HT*PH)+(HE*(PH*1.5)))*(NH*.5))

while True:

     print(menu)
     op=int(input("Ingrese la opcion que desee xd: "))

     if op == 1:
          Ejercicio_1()
     elif op == 2:
          Ejercicio_2()
     elif op == 3:
          Ejercicio_3()
     elif op == 4:
          Ejercicio_4()
     elif op == 5:
          Ejercicio_5()
     elif op == 6:
          Ejercicio_6()
     elif op == 7:
          Ejercicio_7()
     elif op == 8:
          Ejercicio_8()
     elif op == 9:
          Ejercicio_9()
     elif op == 10:
          Ejercicio_10()
     elif op == 11:
          break

import os
import math


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Area del rectangulo
def area_rectangulo_a(base,altura):
    resultado = base * altura
    return resultado

def area_rectangulo_b(base,altura):
    return base * altura

#Invocacion de la funcion

#Mediante la creacion de variables
"""altura = 15
base = 10
area1 = area_rectangulo_a(base,altura)
print(f"1.- El area del rectangulo de {base} * {altura} = {area1}")

#Mediante la captura del resultaado en variable 
area2 = area_rectangulo_a(base,altura)
print(f"2.- El area del rectangulo es = {area2}")

#Invocacion directamente a la funcion
print(f"3.- El area del rectangulo es = {area_rectangulo_a(base,altura)}")"""

#Teclado por usuario

def suma(*args):
    suma_total = 0
    for num in args:
        suma_total += num
    return suma_total

def resta(*args):
    resta_total = 0
    for num in args:
        resta_total += num  #  -1,2,-3,4,5   --->   resta_total = resta_total - num
    return resta_total

def area_circulo(radio=None):
    if radio is None:
        print("El dato ingresado es incorrecto o nulo")
        return
    return  (radio**2) * math.pi

def relacion(num1, num2):
    if  num1 > num2:
        return 1
    elif  num1 < num2:
        return -1
    else:
        return 0

def intermedio(numero_1=None, numero_2=None):
    if numero_1 != None and numero_2 != None:
        intermedio = (numero_1+numero_2)/2
        return intermedio
    else:
        return 0


def recortar(numero_recortar, limite_inferior, limite_superior):
    if  numero_recortar < limite_inferior:
        return limite_inferior
    elif  numero_recortar > limite_superior:
        return limite_superior
    return numero_recortar

def menu():

    while (True):

        print(""" Opciones del menu del sistema
            1.- Sumar
            2.- Restar
            3.- Area de Rectangulo
            4.- Area de Circulo
            5.- Relacion Numeros
            6.- Numero Intermedio
            7.- Recortar
            10.- Salir
        """)
        opcion = int(input("Selecione  un numero para realizar la operacion: \n"))
        if opcion == 1:
            valores = input("Ingrese los numeros que desea sumar, separados por comas: \n") # "1,2,3,4,5"
            args =  tuple(map(int, valores.split(',')))
            sumatoria = suma(*args)
            print(f"La sumatoria de los valores ingresados: {valores} es = {sumatoria}")
            clearConsole()
        elif opcion == 2:
            valores = input("Ingrese los numeros que desea restar, separados por comas: puede utilizar numeros negativos\n") # "-1,2,-3,4,-5"
            args =  tuple(map(int, valores.split(',')))
            resta_total = resta(*args)
            print(f"La sumatoria de los valores ingresados: {valores} es = {resta_total}")
        elif opcion == 3:
            base = float(input("Ingrese la base:\n"))
            altura = float(input("Ingrese la altura:\n"))
            print (f"el area del rectangulo de :  {base} * {altura} =  {area_rectangulo_a(base,altura)} ")
        elif opcion == 4:
            radio = float(input("Ingrese el radio de del circulo:\n"))
            if radio != None:
                print (f"El area del circulo con radio {radio} es = {area_circulo(radio)}")
        elif opcion == 5:
            num1 = int(input("Ingrese el numero 1:\n"))
            num2 = int(input("Ingrese el numero 2:\n"))
            if relacion(num1,num2) == 1 :
                print (f"El numero {num1}  > {num2} ")
            elif relacion(num1,num2) == -1:
                print (f"El numero {num1}  < {num2} ")
            else:
                print (f"El numero {num1}  = {num2} ")
        elif opcion == 6:
            numero_1 = int(input("Ingrese el numero 1:\n"))
            numero_2 = int(input("Ingrese el numero 2:\n"))
            print(f"El numero intermedio de {numero_1}  y {numero_2} es = {intermedio(numero_1,numero_2)}")
        elif opcion == 7:
            numero_recortar = int(input("Ingrese el numero:\n"))
            limite_inferior = int(input("Ingrese el limite inferior:\n"))
            limite_superior = int(input("Ingrese el limite superior:\n"))
            print(f"El resultado es = {recortar(numero_recortar, limite_inferior, limite_superior)}")
        elif opcion == 10:
            break
        else:
            print("La operacion con la opcion enviada no es valida : Error: {opcion}")

#Invocacion al menu principal
menu()


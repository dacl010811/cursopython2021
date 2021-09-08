
import os

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

def menu():

    while (True):

        print(""" Opciones del menu del sistema
            1.- Sumar
            2.- Restar
            3.- Area de Rectangulo
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
            base = float(input("Ingrese la base: \n"))
            altura = float(input("Ingrese la altura: \n"))
            print (f"el area del rectangulo de :  {base} * {altura} =  {area_rectangulo_a(base,altura)} ")
        elif opcion == 4:
            pass
        elif opcion == 10:
            break
        else:
            print("La operacion con la opcion enviada no es valida : Error: {opcion}")

menu()

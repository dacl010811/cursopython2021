#Estructuras de Control

#Condicionales
if True:
    print("Simple")

if True:
    print("Verdadero")
else:
    print("Verdadero")

a = 0
b = 2

if True:
    print("Verdadero")
elif a>0:
    print("Mayor")
elif a<10:
    print("Menor")
elif a!=0:
    print("Distinto")
elif a==1:
    print("Igual")
elif a**2 == 15:
    print("Potencia")
else:
    print("Default")

#Estructuras de Control Repetitivas
# for
for i in range(0,100):
    print("Repetit")

lista = [1,2,3,4,5,6,7,8,9]
#        0 1 2 3 4 5 6 7 8  
diccionario = {'key1':0,'key2':1,'key3':2,'key4':4}
#
for numero in lista:
    print(numero)

for index,numero in enumerate(lista):
    print(numero)

for key,dato in diccionario.items():
    print("{1}:{0}".format(key,dato))

#while
contador = 0
suma = 12

while contador <  100:  # True
    pass

while True:             #Boolean
    if contador == 99:
        break

while (suma*2) != 0 :
    if suma == 100:
        break
    else:
        continue
        print("Hola")

while True:             #Boolean
    if suma == 100:
        break
    else:
        continue
else:
    print("Siempre voy a ejecutar cuando todo vaya bien")

#Funciones

def suma_basica():
    pass

def suma(parametro_1, parametro_2):
    #Variales locales
    suma_total = 0
    suma_total = parametro_1 + parametro_2
    print (suma_total)

#Invocacion
suma(45,54)  # Los datos enviados son los argumentos

def suma_return(parametro_1, parametro_2):
    #Variales locales
    suma_total = 0
    suma_total = parametro_1 + parametro_2
    return suma_total

#Invocacion
variable_1 = suma_return(155,158)
print(variable_1)

#Indeterminados : Tupla y Diccionarios

def suma_indeterminados_listas(*args):
    suma_total = 0
    for numero in args:
        suma_total += numero
    return suma_total

def suma_indeterminados_diccionarios(**Kwargs):
    suma_total = 0
    for key,numero in Kwargs.items():
        suma_total += numero
    return suma_total


#Invocacion tuplas y listas
suma_indeterminados_listas(1,2,3,4,5,6)

tupla1 = (1,2,3,4,5,6)
suma_indeterminados_listas(*tupla1)

#Invocacion sobre  dicionarios
suma_indeterminados_diccionarios(num1=0, num2=10, num3=100, num4=4, num5=5)

dicionario_numeros = {'num1':0, 'num2':10, 'num3':100, 'num4':4, 'num5':5}
suma_indeterminados_diccionarios(**dicionario_numeros)

#Argumentos por defecto 

def suma(parametro_1=0, parametro_2=0):
    #Variales locales
    suma_total = 0
    suma_total = parametro_1 + parametro_2
    print (suma_total)







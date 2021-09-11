#Tipos de datos  en python :  TIPOS PRIMITIVOS
#Literales de tipo String
variable_1 = "Hola"
variable_2 = 'Mundo'
print(type(variable_1))
print(type(variable_2))

#Literales de tipo Numerico :  int y float
# Enteros
variable_1 = 10
variable_2 = 158
print(type(variable_1))
print(type(variable_2))

# Float
variable_1 = 10.77879897
variable_2 = 158.7878
print(type(variable_1))
print(type(variable_2))

#Literales de Boolean

variable_1 = True
variable_2 = False
print(type(variable_1))
print(type(variable_2))

#Datos estructurados

#Listas
lista_numeros = []

#tuplas
lista_numeros = ()

#Diccionarios
lista_numeros = {'clave':0}

#Conjuntos
conjunto_2 = {0}

#Pilas : Basada en listas y utiliza  2 metodos para simular el comportamiento
#Se utiliza los 2 metodos : append y pop para simular el comportamiento de las pilas : LIFO
lista_numeros = [1]
lista_numeros.append(0)
lista_numeros.pop()


#Pilas : Basada en listas y utiliza  2 metodos para simular el comportamiento
#Se utiliza los 2 metodos : append y popleft para simular el comportamiento de las pilas : FIFO
from collections import deque
colas_numeros =  deque([1,2])
colas_numeros.append(0)
colas_numeros.popleft()


#Operaciones con Listas : []
#Listas: Slicing : [index_inicial, index_final, intervalo]
lista_numeros = [1,2,3,4,5,6,7,8,9]
#Indices asc     0 1 2 3 4 5 6 7 8
#Indices desc                -2 -1
sublista1_numeros = lista_numeros[0:4]
sublista2_numeros = lista_numeros[4:8]
sublista3_numeros = lista_numeros[-1]
print(sublista1_numeros)
print(sublista2_numeros)
print(sublista3_numeros)

#Lista numeros impares
sublista4_numeros = lista_numeros[::2]
print(sublista4_numeros)
# Listas numeros pares
sublista5_numeros = lista_numeros[1::2]
print(sublista5_numeros)
#Respaldar los tipos de datos por referencia
backup_lista = lista_numeros[:]

backup_lista.pop()
backup_lista.pop()

#Acceder a metodos de los tipos de datos estructurados

#backup_lista.clear()
backup_lista_1 = backup_lista.copy()

print("Backup_lista1 ",backup_lista_1)
print("Original",lista_numeros)
print("backup", backup_lista)

#Sacar respaldos de datos x referencia
backup_lista_1 = backup_lista.copy()
backup_lista = lista_numeros[:]

backup_lista_1.clear()
print("Backup_lista1_clear() ",backup_lista_1)

lista_numeros = [100,-12,-1,15,1,1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9]
backup_lista_1 =  lista_numeros[:]
numero_buscar = 1
numero_ocurrencias = backup_lista_1.count(numero_buscar)
print("El numero de ocurencias del #{0} es = {1}".format(numero_buscar,numero_ocurrencias))

#Sort. Ordenamiento
lista_letras = ['z','Z','b','c','d','e','f','g','h','h','x']
lista_letras.sort()
print(lista_letras)

#Remover la primera coincidencia de un numero a eliminar
lista_numeros = [100,-12,-1,15,1,1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9]
lista_numeros.remove(9)
print(f"Lista Original tiene : {len(lista_numeros)} ")
print(lista_numeros)
print(f"Lista Final tiene  : {lista_numeros.count(9)} ")

#Tuplas
tupla_1 = (100,-12,-1,15,1,15)
#Index      0    1  2  3  4 5
print(type(tupla_1))
print (tupla_1.index(-1))
print (tupla_1.count(15))

print("---- Dicionarios------")
#Dicionarios
try:
    diccionario1 = {'name':'Darwin', 'ape':'Calle','lenguaje':'python','15':'89/100','lista_cedulas':['1100458791', '11004587917']}
    lista_2 = []

    for key in diccionario1:
        dato = diccionario1[key]
        lista_2.append(dato)

    lista_dic = list(diccionario1)
    print("dic convertido",lista_dic)
    print("dic convertido datos",lista_2)

    print(diccionario1['lista_cedulas'])

except KeyError:
    print(f"Error Controlado: KeyError")
except Exception as e:
    print(f"Error : {type(e).__name__} ")

#Metodos de los dicionarios
print("Keys")
print (diccionario1.keys())
print (diccionario1.values())
print("Dic Original ", diccionario1)
for i  in range(0, len(diccionario1)):
    diccionario1.popitem()
print("Dic Final ", diccionario1)






















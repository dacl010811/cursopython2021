#Tuplas son Inmutables :  NO se pueden cambiar los datos que contiene dicha estructura

tupla_1 = (1,2,3,4,5,6,7,8,9,10)  # tupla de enteros

tupla_2 = (True, False) # tupla de boolean

tupla_3 = (5.2, 7.4) # tupla de float

tupla_4 = ('True', "False") # tupla de String

tupla_5 = (1, 4.5, 'Hola', [1,2,3], (5,6,7) ) # tupla de Mix
#Indices   0   1      2        3       4

print(type(tupla_1))
print(tupla_1)

print(type(tupla_2))
print(tupla_2)

print(type(tupla_3))
print(tupla_3)

print(type(tupla_4))
print(tupla_4)

print(type(tupla_5))
print(tupla_5)

# Para obtener los elementos de las tuplas vamos a utilizar sus indices
print("Elemento posicion", tupla_5[2])

#Slicing de tuplas :  Extraer subTuplas
print("Slicing")
tupla_5 = (1, 4.5, 'Hola', [1,2,3], (5,6,7) ) # tupla de Mix
print("Elemento posicion", tupla_5[0:3])
print("Elemento posicion", tupla_5[0:3][2])

#Inmutabilidad
#lista_total_1 =  tupla_1 + tupla_2

#Artificios conversiones de Listas a tuplas
lista_total =  list(tupla_1) + list(tupla_2)
tupla_final =  tuple(lista_total)
print(type(lista_total))

#Cambiar elementos
tupla_5 = (1, 4.5, 'Hola', [1,2,3], (5,6,7) ) # tupla de Mix

print("Caso 1")
print(tupla_5[3][1])
tupla_5[3][1] = 22

print("Caso 2")
print(tupla_5[3])
#tupla_5[3] = [11,22,33]  #Inmutabilidad

print("Caso 3")
print(tupla_5[4][1])
#tupla_5[4][1] = 66 #Inmutabilidad

print(tupla_5)

#append() en tuplas : Agregar elementos a la tupla no se puede realizar por  caracteristica de la Inmutabilidad
#tupla_5.append("Python 3")
print(tupla_5)

#Funciones de las tuplas :  len(), index(), count()
tupla_5 = ('Hola', 1, 4.5, 'Hola', [1,2,3], (5,6,7), "Hola" ) # tupla de Mix

print("La tupla tiene f len() :", len(tupla_5))            #Determina el numero de elementos de la tupla()

print("La tupla tiene f count():", tupla_5.count('Hola'))  #Devuelve el numero de ocurrencias del dato enviado a la funcion count() 

print("La tupla tiene f index():", tupla_5.index('Hola'))  # Devuelve la posicion (indice) del elemento a buscar; la primera ocurrencia





#Dicionarios  su principal caracteristica es :   key:Valor
# No se pueden repetir las llaves o keys
# las  llaves o keys se deben trabajar  en lo posible con datos de tipo string

#Definir los diccionarios
diccionario =  {}
print(type(diccionario))
print(diccionario)

diccionario =  {'amarillo':'yellow', 'azul':'blue', 'rojo':'red', 'cero':0.5, 'True':True,'False':False}
print(type(diccionario))
print(diccionario)

#Acceder a los elementos es atravez de su llave o key

valor = diccionario['amarillo']
print(valor)
print(type(valor))

valor1 = diccionario['cero']
print(valor1)
print(type(valor1))

valor2 = diccionario['True']
print(valor2)
print(type(valor2))

#Modificar los elementos del dicionario mediante la llave o Key------>     (k,v)
diccionario['amarillo'] =  'black'
print(diccionario)

diccionario['rojo'] =  'Python'
print(diccionario)

diccionario['True'] =  1
print(diccionario)

diccionario['False'] =  0
print(diccionario)

#Vamos añadir elementos al diccionario ya definido
diccionario['verde'] =  'green'
print(diccionario)

diccionario['rojo1'] =  'Python3'
print(diccionario)

diccionario['green'] =  'Python3'
print(diccionario)

# Llaves de tipo Entero
print("Laves de tipo numerico")
numeros = {'0':0.5, '1':11, '2':22, '3':33 }

print(numeros['0'])
print(numeros['1'])

#Eliminar elementos
print("Eliminar elementos del diccionario")
numeros = {'0':0.5, '1':11, '2':22, '3':33 }
del(numeros['0'])
del(numeros['1'])

print(numeros)

#Combinacion de operadores aritmeticos y de asignacion:      +=, -=, *= etc

print("Operaciones sobre elementos del diccionario")
numeros = {'0':0.5, '1':11, '2':22, '3':33 }
numeros['1']+=100
numeros['2']-=100
numeros['3']**=5
print(numeros)

#Recorrido de los elementos de un diccionario

print("Recorrec un dicionario")
for key in numeros:
    print(f" key:{key}  : {numeros[key]} ")


#Recorrido de los elementos de un diccionario

print("Recorrec un dicionario")
for key,valor in numeros.items():
    print(f" key:{key}  : {valor} ")





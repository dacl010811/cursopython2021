#Son colecciones desordenadas  y tiene elementos unicos

#Forma 1 mediante la clase set()
conjunto = set()
print(type(conjunto))
print(conjunto)

#Forma 2 mediante los caracteres  "{valor}"   Sirve para representar diccionarios {clave:valor}

conjunto_2 = {5,1,2,3}
print(type(conjunto_2))
print(conjunto_2)

#Agregar ELementos a un conjunto
conjunto_2.add(4)
conjunto_2.add(4)
conjunto_2.add('A')
conjunto_2.add('Z')
conjunto_2.add('C')
conjunto_2.add('A1')
conjunto_2.add('A')
conjunto_2.add('Z')
conjunto_2.add('C')
conjunto_2.add('A1')
conjunto_2.add('A')
conjunto_2.add('Z')
conjunto_2.add('C')
conjunto_2.add('A1')

# funcion in() :  Sirve para determinar si un elemento pertenece al conjunto
#conjunto_2 = {5,1,2,3}

grupo = {2,6,5}
print("--- funcion in ()-----")
resultado_1 =  5 in grupo   # verdadero o Falso
print(resultado_1)
print(grupo)

print("--CASTING--")
#Casting
lista = [1,2,3,4,5,6,7,7,1,2,3,9,10]
print(lista)
print(type(lista))

conjunto_cast = set(lista)
print(type(conjunto_cast))
print(conjunto_cast)

# Casting String a SET o conjunto
print("---- Casting de String a Set o  {}")
cadena_original =  "Python es un lenguaje flexible, lenguaje facil, es fabuloso"
print(type(cadena_original))

conjunto_string  = set(cadena_original)

print(conjunto_string)
print(type(conjunto_string))

# Casting  de  conjunto a una  lista

lista_mensaje = list(conjunto_string)
print(lista_mensaje)

lista_mensaje = tuple(conjunto_string)
print(lista_mensaje)

#Obtener los elemtos
conjunto_string = {2,6,5}
for elemento in conjunto_string:
    print(elemento)




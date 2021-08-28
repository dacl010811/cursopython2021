# Listas en python

lista_enteros = [1,2,3,4,5]   # Lista de Enteros

lista_floats = [1.0,2.0,3.5,4.5,5.5]  # Lista de Floats

lista_cadenas = ["A","B",'C','SE',"HO"]  # Listas de String

lista_general  = [1, 3.5, "Cadena1", True, [1,2,3,4] ] #  Lista de tipo  multiple
#                 0   1       2        3
#Aceder a los elementos de la lista: Se lo realiza mediante los indices :  Posicion 0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9, n

print(lista_enteros[0],lista_enteros[-1])
print(lista_enteros[1],lista_enteros[-2])
print(lista_enteros[2])

# Slicing de  listas en python

# Lista principal :  lista_enteros

sub_lista_1 =  lista_general[0:2]
sub_lista_2 =  lista_general[2:]

print(sub_lista_1)
print(type(sub_lista_1))

print(sub_lista_2)
print(type(sub_lista_2))

print("--------")
print(type(lista_general))

# Operaciones con listas
#Suma   "+"

impares = [1,3,5,7,9]
pares = [2,4,6,8,10]

lista_total = impares + pares
print(lista_total)
print(type(lista_total))

#Modificar los elementos de la lista
#[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# 0  1   2

lista_total[1] = 2
lista_total[2] = 3
lista_total[3] = "S"
lista_total[4] = True

print("Mi nueva lista es : \n")
print(lista_total)

#Agregar Elementos a un lista

lista_general  = [1, 3.5, "Cadena1", True, [1,2,3,4] ]
print(f"Lista Original es : {lista_general}")

lista_general.append("Darwin")
print(f"Lista Modificada es : {lista_general}")

lista_general.append("Calle")
print(f"Lista Modificada es : {lista_general}")

lista_general.append(8+15)
print(f"Lista Modificada es : {lista_general}")

lista_general.append( (8+15)* 2 + (10/2) )
print(f"Lista Modificada es : {lista_general}")

lista_nueva = [True, False]

lista_general.append( lista_nueva )
print(f"Lista Modificada es : {lista_general}")


print(len(lista_general))

print(lista_general[len(lista_general)-1])









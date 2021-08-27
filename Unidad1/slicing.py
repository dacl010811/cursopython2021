#Slicing : Extraer subcadenas de una cadena principal
palabra = "Hola Mundo"
#          0123456789
#         10987654321

print(len(palabra))
print(palabra[0:2])
print(palabra[:2])  # Indica a python que empiece desde 0
print(palabra[2:])  # indicamos a python  que termine hasta el final de la cadena

print("---------------")
print(palabra[:])    #Significa traer  toda la cadena


print("---------------Slicing Negativo -------------------")


palabra = "Python Hola Programacion Mundo"
variable1 = "Hola"   #Slicing 1 
variable2 = "Mundo"  #Slicing  2

print(f"Python es un lenguaje {variable1} {variable2}")   #Python 3  Recomendada
print("Python es un lenguaje {0} {1}".format(variable1,variable2)) #Python 2.x
print("Python es un lenguaje {} {}".format(variable1,variable2)) #Python 2.x


#type()  Ver el tipo de dato
#print()  Imprimir en pantalla
#Determinar la languitud de un objeto str
#Longitud de la cadena

print("---- Len------")
palabra = "Python Hola Programacion Mundo"
print(len(palabra))
print(palabra[0:len(palabra)])

#Inmutabilidad de las cadenas

print("Inmutable")

cadena_i = "python"
cadena_i[0] = "P"

print(cadena_i)

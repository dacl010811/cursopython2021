#Definir cadenas o String (
#

cadena_1 = "Mi pelicula favorita es :"   # Tipado dinamico  :
cadena_2 = "Avangers"

# Para concatenar utilizamos   signo "+"

cadena_3 = cadena_1 + " " +cadena_2

print(type(cadena_3))
print(cadena_3)

# Concatenar tambien vamos utilizar  ","


cadena_1 = "100"
cadena_2 = "Mazda"
cadena_3 = "Toyota"

#Primera Forma
cadena_4 = cadena_1+cadena_2+cadena_3

#cadena_4 = cadena_1,cadena_2,cadena_3

#print(type(cadena_4))
print("Primera Forma"+" "+cadena_4)

#Segunda forma
suma = 5 + 5 + 300.2356565
print("El valor de la suma Forma2",round(suma,4))

#Tercera Forma
print(f"La cadena final es Form3 : {suma}, {cadena_1} , {cadena_2}, {cadena_3}")

#Cuarta Forma
print("La cadena final es Forma4 : {}, {} , {}".format(suma,cadena_1,cadena_2,cadena_3))


#Print de caracteres especiales: Se utiliza para dar formato a las cadenas o strings
# \n \r \t
print("Menu \t Principal 1.- Suma :  2.- Resta")

print(r"C:\Users\Tdelita\nercop\rombre") #raw

#Impimir Multilinea

print("Una linea\nsegunda linea\ntercera linea\ncuarta linea\n")

print("""Una linea
segunda linea
tercera linea
cuarta linea""")

#Operacion multiplicacion  (*)

cadena_1 = "*"
cadena_2 = "C:NombreCarpeta\n"

cadena_3 =  10 * "***\t"
print(cadena_3)

# Indices en las cadenas

# "P   Y   T   H   O   N"
#  0   1   2   3   4   5  >>>>>>> Ascendente
#  -6    -5    -4    -3    -2   -1 >>>Descendente

CADENA= "ESTE PYTHON2"

print(CADENA[1],CADENA[5],CADENA[6])
print(CADENA[1])
print(CADENA[2])
print(CADENA[3])


#Slicing : Extraer subcadenas de una cadena principal
palabra = "Hola Mundo"
#          0123456789

print(len(palabra))
print(palabra[0:10])































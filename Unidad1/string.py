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
print("Menu Principal 1.- Suma :  2.- Resta")

print(r"C:\Users\Tdelita\nercop\rombre") #raw

#Impimir Multilinea

print("Una linea\nsegunda linea\ntercera linea\ncuarta linea\n")

print("""Una linea
segunda linea
tercera linea
cuarta linea""")



















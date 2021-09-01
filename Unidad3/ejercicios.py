# Verificar notas
# Rango :    0  a 5 : perdiste el año
# Rango :    6  a 7 : Supletorio
# Rango :    8  : Bueno
# Rango :    9 : Muy Bueno
# Rango :    10 : Sobresaliente

nota_final =  int (input("Ingresa la nota de tu examen : \n"))

if nota_final >= 0 and nota_final <= 5:
    print("Perdiste de Año")
elif nota_final >= 6 and nota_final <= 7:
    print("Te vas a supletorio")
elif nota_final == 8:
    print("Bueno")
elif nota_final == 9:
    print("My Bueno")
elif nota_final == 10:
    print("Sobresaliente")
else:
    print("La opcion enviada no existe!!!! Lo siento")

#Ejercicio para determinar si un numero es PAR o IMPAR
# Piderle al usuario el ingreso de numero por teclado
# Verificar si el # ingresado es PAR o IMPAR y preentar el mensaje en pantalla
# Operadores de Comparacion :  MOD, Resto



#Ejercicio : Determinar si la edad de una persona  que ingresa  es mayor de EDAD
#Definir constante de la EDAD:    ADULTO >= 18 imprimir en pantalla : "Eres mayor de Edad"



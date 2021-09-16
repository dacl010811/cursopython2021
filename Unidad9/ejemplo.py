
#

def tarea1():
    lista = []
    numero_emcontrado = 8

    while True:
        numero = input("Ingrese el numero de 0/9")
        lista.append(numero)
        for numero in  lista:
            if numero == numero_emcontrado:
                print("Encontrado")
                break

def tarea7():
    lista1 = [1,2,3,4,5,6,2,4]            #2 4

    lista2 = [11,2,13,4,15,16,2,4]         #2 4
    lista_final = []

    for numerol1 in lista1:
        for numerol2 in lista2:
            if numerol1 == numerol2:
                lista_final.append(numerol1)

    print(lista_final) #2 4 2 4
    conjunto = set(lista_final)
    print(conjunto) #2 y 4






# Valores por Valor

def resta(a=None,b=None):

    if a != None and b != None:
        if isinstance(a,int) and isinstance(b,int):
            resultado = a-b
        else:
            print("Error, no se pueden realizar operacion con datos que no sean Base10")
            return
    else:
        print("Los datos enviados son nulos")

    return resultado

resta(10,5)

# Paso  por referencia :   Se aplican directamente a las estructuras como listas, tuplas, diccionario

def duplicar_numeros(numeros):

    if isinstance(numeros,tuple):
        temp_lista = list(numeros)
        for i,n in enumerate(temp_lista):
            temp_lista[i] *= 2
        numeros = tuple(temp_lista)
        print(numeros)

numeros = (10,20,30,40)
print("Lista Inicial", numeros)
duplicar_numeros(numeros)





#Funciones con retorno de valor.

def  suma(a,b):
    suma_total = a + b
    return suma_total   # Cualquier tipo de dato : int, float, String, [[]], (), {a,b},{a:9, b:4545}

#Invocacion por nombre del parametro
total = suma(b=100,a=500)
total_1 = suma(a=25011,b=11700)


# Funciones con return de tipo de dato String

def  saludar(nombre, apellido):
    nombres_completos = nombre +" "+apellido
    return nombres_completos   #Str  o String

print(f" El resultado 1 es = {total}")
print(f" El resultado 2 es = {total_1}")

#cadena = saludar('Darwin','Calle')
print(f"Hola {saludar('Darwin','Calle')}, estamos aprendiendo python")


# Retorno de valor multiple

def saludar_multiple():
    """Return multiple

    Returns:
        [tuple]: Tupla de  varios tipos de dato
    """
    nombre = "Darwin"
    apellido = "Calle"
    profesion = "Ing"

    return  "Hola",nombre,apellido,profesion,[10,34.5,True],(1,2,3),{'a':'A'}
#              0      1       2        3

#Asignicacion de variables en una sola linea: Posicional

var_1, var_2 = saludar_multiple()[0], saludar_multiple()[1]


print(var_1)
print(var_2)

#Envio de valores

def  suma(a,b):
    suma_total = a + b
    return suma_total   # Cualquier tipo de dato : int, float, String, [[]], (), {a,b},{a:9, b:4545}

#Invocacion por nombre del parametro
total = suma(100,500)
total_1 = suma(a=25011,b=11700)




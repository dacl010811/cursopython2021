
#   def +  nombre descriptivo + :

#Definir las variables globales al inicio de  la clase
global a

def saludar_vacio():
    print(f"Hola mundo desde una funcion python")

def saludar(nombre):
    print(f"Hola mundo: {nombre} desde una funcion python")
    print(nombre*10)
    print(nombre[0:5:2])

def despedida():
    pass

def sumar():
    pass

def restar():
    pass


#Realizar la llmada a la funcion saludar

#saludar_vacio()
#saludar("Darwin Calle")
saludar("Darwin Calle")

#Imprima las tablas de multiplcar
def crear_tabla_multiplicar(tabla):
    """Crear un tabla de multiplicar dado el numero de la tabla
    Args:
        tabla (int): Corresponde a la tabla de multiplicar
    """
    for numero in range(1,11,1):
        print(f"{tabla} * {numero} = {tabla*numero}")

def crear_tabla_multiplicar_1(tabla,limite):
    """Crear un tabla de multiplicar dado el numero de la tabla
    Args:
        tabla (int): Corresponde a la tabla de multiplicar
    """
    #Variables locales
    b = 15
    c = 125
    a = 155555555555

    for numero in range(1,limite+1,1):
        print(f"{tabla} * {numero} = {tabla*numero}")



#crear_tabla_multiplicar(8)

#Invocacion  posicional
crear_tabla_multiplicar_1(4,10)

#Invocacion  por nombre de variable
crear_tabla_multiplicar_1(limite=25, tabla=7)

a = 123
print(a)






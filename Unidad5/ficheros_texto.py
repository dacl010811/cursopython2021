from io import open

def crear_fichero(nombre_archivo):
    fichero = open(nombre_archivo,'w')
    fichero.close()

"""crear_fichero('hola.txt')
crear_fichero('hola.doc')
crear_fichero('hola.csv')
crear_fichero('hola.xls')
crear_fichero('hola.dat')
crear_fichero('hola.py')"""

#Crear el fichero vamos a escribir sobre este

def crear_fichero_w(nombre_archivo):
    texto = "2.-Esta es una linea para el archivo"
    fichero = open(nombre_archivo,'w')
    fichero.write("") #
    fichero.close()

#crear_fichero_w('hola.txt')

# Lectura total del fichero con el metodo read()
def leer_fichero_r(nombre_archivo):
    fichero = open(nombre_archivo,'r')
    contenido = fichero.read()
    fichero.close()
    print(f"El contenido del fichero es : \n {contenido}")

#leer_fichero_r('hola1.txt')

# Lectura del fichero con el metodo readLine() -->> Lectura linea a linea
def leer_fichero_readLine(nombre_archivo):
    fichero = open(nombre_archivo,'r')
    cadena = ''
    for  linea in range(10):
        cadena += fichero.readline()

    fichero.close()
    print(f"El contenido del fichero es : \n {cadena}")

#leer_fichero_readLine('hola.txt')


# Lectura del fichero con el metodo readLines() -->> Lectura linea a linea
def leer_fichero_readLines(nombre_archivo):
    fichero = open(nombre_archivo,'r')
    lista_lineas = fichero.readlines()
    fichero.close()

    print("El contenido del archico es : \n")
    for index,linea in enumerate(lista_lineas):
        print(f"[{index}] : {linea}")

#leer_fichero_readLines('hola.txt')

#Append : Agregar contenido al final del archivo

def agregar_lines_fichero(nombre_archivo):
    fichero = open(nombre_archivo,'a')
    fichero.write("\nEste es un programa hecho python.")
    fichero.close()

#for linea in range(0,100001):
#    agregar_lines_fichero('hola.txt')

# Gestion de archivos mediante  el metodo with: Recursos Gestionados Automaticamente

def  leer_archivo_with(nombre_archivo):
    with  open(nombre_archivo,'r') as fichero:
        for linea in fichero:
            print(linea)

#leer_archivo_with('hola.txt')

#Lectura y escritura a la vez

def  lectura_escritura_a_la_vez(nombre_archivo):
    fichero = open(nombre_archivo,'r+')
    fichero.write("Nueva Linea")
    fichero.close()

#lectura_escritura_a_la_vez('hola.txt')

def  lectura_escritura_a_la_vez_2(nombre_archivo):
    fichero = open(nombre_archivo,'a+')
    linea_nueva = "Nueva Linea al final\n"
    fichero.write(linea_nueva)
    fichero.close()

for  repetir in range(1,11):
    lectura_escritura_a_la_vez_2('hola.txt')












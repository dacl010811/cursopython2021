#Primera forma de importar nuestros modulos

#from saludos import  saludar
#from saludos import  VARIABLE_GLOBAL
#from saludos import  Hola

#Segunda forma
#Importacion desde un  MODULO
#from saludos import saludar
#from saludos import Hola
#from saludos import VARIABLE_GLOBAL
#from saludos import *

#Importacion desde un PAQUETE
from modulospy.saludos import saludar
from modulospy.saludos import Hola
from modulospy.saludos import VARIABLE_GLOBAL

#Seccion de Invocacion
saludar("Darwin Augusto Calle L")
hola = Hola("Juan")
hola.saludar()


def recortar(numero_recortar,limite_inferior, limite_superior):

    if  numero_recortar < limite_inferior:
        return limite_inferior
    elif numero_recortar > limite_superior:
        return limite_superior
    else:
        return numero_recortar

#Invocacion
print (recortar(15,0,10)) #10



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
saludar("Darwin Calle")
hola = Hola("Juan")
hola.saludar()

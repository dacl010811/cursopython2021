#Variables Global
VARIABLE_GLOBAL = 'Python3'

def  saludar(nombre):
    if nombre:
        print(f"Hola como estas {nombre}")

class  Hola():
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Bienvenido desde la clase : Hola {self.nombre}")

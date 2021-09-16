#Encapsulamiento

class Ejemplo():
    #Atributo de clase
    __atributo_privado_a = "Python A"
    __atributo_privado_b = "Python B"

    def __init__(self, nombre):
        self.__nombre = nombre

    #get de un atributo
    @property
    def nombre(self):
        return self.__nombre

    #Simular un set
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f'Objeto de tipo Ejemplo {self.__atributo_privado_b}'

    def __metodo_privado_ejemplo(self):
        print("Soy un metodo privado")

    #Simular get A
    def atributo_publico_a(self):
        return self.__atributo_privado_a

    #Simular get B
    def atributo_publico_b(self):
        return self.__atributo_privado_b

    def set_publico_a(self,valor):
        self.__atributo_privado_a = valor

    def set_publico_b(self,valor):
        self.__atributo_privado_b = valor

#Invocacion de Atributos de Clase
#print(Ejemplo.__atributo_privado_a)
#print(Ejemplo.__atributo_privado_b)

#Segunda invocacion  por medio  de un objeto
ejemplo = Ejemplo("Ejmeplo1")
#print (ejemplo.__atributo_privado_a)
#print (ejemplo.__atributo_privado_b)
print (ejemplo.atributo_publico_a())
print (ejemplo.atributo_publico_b())

print("------ SET ----")

ejemplo.set_publico_a('Java A')
ejemplo.set_publico_b('Java B')

print (ejemplo.atributo_publico_a())
print (ejemplo.atributo_publico_b())

print ("================================")
print (ejemplo.nombre)
try:
    print (ejemplo.__nombre)
except Exception as e:
    print(f"Error : {type(e).__name__}")

print ("Set metadata")
ejemplo.nombre = 'Ejemplo2 SET'
print (ejemplo.nombre)





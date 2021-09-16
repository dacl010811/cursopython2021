class Persona():

    #Atributos de Clase
    CI = ''

    #Constructor
    def __init__(self, nombre, apellido, celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.email = email

    def __str__(self):
        return f'Objeto Persona : {self.nombre} {self.apellido}'

    # El metodo que tiene la  referencia self es un metodo de instancia
    def caminar(self):
        print("Estoy caminando")

    def comer(self):
        print("Estoy comiendo")

    def acelerar():
        print("Acelerando...!!!!")

#Invocacion  de la clase persona
persona_1 = Persona('Darwin','Calle','0998744522','dacl010811@hotmail.com')
print(persona_1)
print('Llamando a los metodos')
#Metodos de instancia
persona_1.caminar()
persona_1.comer()

#Invocacion de un metodo de clase
Persona.acelerar()

#Atributos dinamicos
persona_1.telefono = '02248752'
persona_1.pasaporte = 'AE015421'
persona_1.ruc = '1100487520001'

print("Atributos dinamicos")
print(persona_1.telefono)
print(persona_1.pasaporte)
print(persona_1.ruc)

#Modificacion
persona_1.nombre = 'Santiago'
print(persona_1)








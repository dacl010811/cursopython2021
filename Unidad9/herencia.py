

class Animal():

    TIPO = ''

    def __init__(self):
        pass

    def dormir(self):
        print("Puedo dormir desde la superclase : Animal")

#SuperClase :
class Persona():

    #Atributos de Clase
    CI = ''
    PASAPORTE = ''
    DIRECCION = ''
    CELULA = ''

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

class Empleado(Persona, Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Soy un objeto de tipo EMPLEADO : {self.nombre}'


class Funcionario(Persona, Animal):

    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def __str__(self):
        return f'Soy un objeto de tipo FUNCIONARIO : {self.nombre} {self.institucion} '


#Instanciar objetos
persona_1 = Persona('Darwin','Calle','0998744522','dacl010811@hotmail.com')
print(persona_1)


print("=======Empleado================")

empleado_1 = Empleado('Empleado1')
empleado_1.CELULA = '1102588524'
empleado_1.TIPO = 'MAMIFERO'
print(empleado_1)
print(empleado_1.CELULA)
print(empleado_1.TIPO)
empleado_1.comer()
empleado_1.caminar()
empleado_1.dormir()

print("\n")
print("===Funcionario===")

funcionario_1 = Funcionario('Funcionario1', 'SRI')
funcionario_1.CI = 'ATRFVAF'
funcionario_1.TIPO = 'AVE'
print(funcionario_1)
print(funcionario_1.CI)
print(funcionario_1.TIPO)
funcionario_1.caminar()
funcionario_1.comer()
funcionario_1.dormir()



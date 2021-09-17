class Vehiculo():

    __anno_fabricacion = ''

    #Constructor for Vehiculo
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Soy un objeto: Vehiculo:\n{self.color}\n{self.ruedas}\n\n'

    def frenar(self):
        print("Frenando....: Clase Vehiculo ")

    def arrancar(self):
        print("Arranco : Clase Vehiculo")

class Automovil(Vehiculo):

    #Constructor for Vehiculo
    def __init__(self,color,ruedas,velocidad,cilindraje):
        #Vehiculo.__init__(self,color,ruedas) # Significa que estoy haciendo referencia a los atributos de la superclase
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return f'Soy un objeto: Automovil:\nVelocidad: {self.velocidad}\nCilindraje: {self.cilindraje}\nColor: {self.color}\nRuedas: {self.ruedas}\n\n'


class Camion(Vehiculo):

    #Constructor for Vehiculo
    def __init__(self,capacidad,origen_fabricacion):
        self.capacidad = capacidad
        self.origen_fabricacion = origen_fabricacion

    def __str__(self):
        return f'Soy un objeto: Camion:\nCapacidad: {self.capacidad}\nOrigen Fabricacion: {self.origen_fabricacion}\n\n'


class Bicicleta(Vehiculo):

    ruedas = 2
    #Constructor for Vehiculo
    def __init__(self,tipo):
        self.tipo = tipo

    def __str__(self):
        return f'Soy un objeto: Bicicleta:\n{self.tipo}\n\n'

class Motocicleta(Vehiculo):

    #Constructor for Vehiculo
    def __init__(self,marca):
        self.marca = marca

    def __str__(self):
        return f'Soy un objeto: Motocicleta:\n{self.marca}\n\n'


#Instanciar
automovil = Automovil('verde',4,'150KM/h','2.2')
print(automovil)

#camion = Camion('4T','CHINA')
#print(camion)

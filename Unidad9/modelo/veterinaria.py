class Persona():
    def __init__(self,email,direccion,telefono):
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

class Fisica(Persona):
    def __init__(self,email,direccion,telefono,DNI):
        super().__init__(email,direccion,telefono)
        self.DNI = DNI

class Juridica(Persona):
    def __init__(self,email,direccion,telefono,CIF):
        super().__init__(email,direccion,telefono)
        self.CIF = CIF



#POO
class Cliente():

    #Definiendo un Constructor
    def __init__(self,nombre,apellido,direccion,ruc,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.ruc = ruc

    def __str__(self):
        return 'Mi Objeto tipo Cliente : {} {} {}'.format(self.nombre, self.apellido,self.ruc)

class Empresa():

    #Constructor
    def __init__(self,nombre,direccion,ruc,clientes=[]):
        """Crea objetos de tipo Empresa

        Args:
            nombre (str): Nombre de la empresa.
            direccion (str): Direccion de la empresa
            ruc (str): Ruc de la empresa
            clientes (list, optional): Lista de clientes de la empresa. Defaults to [].
        """
        self.nombre = nombre
        self.direccion = direccion
        self.ruc = ruc
        self.clientes = clientes

    def __str__(self):
        return 'Mi Objeto tipo Empresa : {} {} {}'.format(self.nombre, self.direccion,self.ruc)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente.nombre)

    def mostrar_cliente(self, ruc_a_buscar):
        for cliente in self.clientes:
            if cliente.ruc ==  ruc_a_buscar:
                print(f"Si existe el ruc # : {cliente.ruc}")
                return
            else:
                print("El cliente a mostar no existe!!!")

    def agregar_cliente(self, clientes=[]):
        try:
            for index,cliente in enumerate(clientes):
                self.clientes.append(cliente)
        except Exception as e:
            print(f"Error al agregar cliente: {type(e).__name__}")

    def agregar_clientes(self, *args):
        try:
            for index,cliente in enumerate(args):
                self.clientes.append(cliente)
        except Exception as e:
            print(f"Error al agregar cliente: {type(e).__name__}")

    def borrar_cliente(self,ruc_borrar):
        for index,cliente in enumerate(self.clientes):
            if cliente.ruc == ruc_borrar:
                del(self.clientes[index])
                print(F"El cliente con RUC: {cliente.ruc} fue  borrado satisfactoriamente")
                return
            else:
                print("El cliente a eliminar no existe!!!")


#Crear objetos de Cliente
cliente_1 = Cliente('Darwin','Calle','La Kennedy','1700587451001','0997744144','dacl010811@hotmail.com')
cliente_2 = Cliente('Adela','Calle','La Kennedy','1107858524001','0997744144','dacl010811@hotmail.com')
cliente_3 = Cliente('Alexandra','Calle','La Kennedy','1107858524001','0997744144','dacl010811@hotmail.com')


print(cliente_1)


#Crear o Instanciar objetos de tipo Empresa

empresa_1 = Empresa('ABACOM','Loja-Ecuador','1104584587001',clientes=[cliente_1,cliente_2,cliente_3])
print (empresa_1)
empresa_1.mostrar_cliente('1700587451001')
print ("Empresa Inicial")
empresa_1.mostrar_clientes()

cliente_4 = Cliente('Nicolas','Calle','La Kennedy','1107858524001','0997744144','dacl010811@hotmail.com')
cliente_5 = Cliente('Cesar','Calle','La Kennedy','1107858524001','0997744144','dacl010811@hotmail.com')

empresa_1.agregar_cliente([cliente_4,cliente_5])
print ("Empresa Final")
empresa_1.mostrar_clientes()



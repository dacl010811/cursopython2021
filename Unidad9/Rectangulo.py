class Rectangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = float(input("Ingrese la base del rectangulo: \n"))
altura = float(input("Ingrese la altura  del rectangulo: \n"))

#Primera instancia de rectangulo
rectangulo_1 =  Rectangulo(base, altura)
area_rectangulo = rectangulo_1.calcular_area()
print(f"El area del rectangulo de {base} * {altura} = {area_rectangulo}")

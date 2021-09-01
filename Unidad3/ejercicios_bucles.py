serie = int(input("Ingresar el limite de la serie \n"))
contador = 0

while  contador < serie:
    contador +=1
    if not (contador %  2 == 0):
        continue
    print(f"# {contador} :")
else:
    print(f"La serie de pares esta correcta")

print("Fin del programa")


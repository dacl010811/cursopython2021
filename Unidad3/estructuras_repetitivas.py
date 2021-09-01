# Estructura While

bandera = True
contador = 1 # Float Int = 1

while contador <= 10:
    print(f" {contador} : Hola Mundo:")
    contador += 1

# While-else :   continue y break
print("************************While-Else**************************")
contador = 1

while contador <= 5:
    print(f" {contador} : Hola Mundo:")
    contador += 1
else:
    print("La estructura while se ejecuto correctamente!!!!")

# Break
print("-----------------While-break----------------")
contador = 1
while contador <= 20:
    print(f" {contador} : Hola Mundo:")
    if contador == 10:
        pass
    contador += 1
else:
    print("La estructura while se ejecuto correctamente!!!!")

# Continue
print("-----------------While-Continue----------------")
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(f" {contador} : Hola Mundo:")
else:
    print("La estructura while se ejecuto correctamente!!!!")



#  Estructura for
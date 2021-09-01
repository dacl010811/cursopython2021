# For :  Iterar entre elemento y elemento
lista = [1,2,3,4,5,6,7,8,9]
#        0 1 2 ..........

print("-------------Estructura While------------")

indice = 0
while (indice < len(lista)):
    print(f"{indice} : {lista[indice]}")
    indice +=1

#Cambios para el estructura for
print("-------------Estructura For------------")
indice = 0
for dato in lista:
    print(f"{indice} : {dato}")
    indice += 1

#For  se puede combinar con metodo llamdo : enumerate
print("-------------Estructura For con metodo enumerate()------------")

lista = [1,2,3,4,5,6,7,8,9]
#indices 0 1 2 ........... 

#(0,1)
#(1,2)
#(2,3)

for index,dato in enumerate(lista):
    print(f"{index} : {dato}")

#For  se puede combinar con metodo llamdo : range()

print("-------------Estructura For con clase range()------------")
for dato in range(11):
    print(f" F1 {dato}")

for dato in range(1,11):
    print(f" F2 {dato}")

for dato in range(2,11,3):
    print(f" F3 {dato}")


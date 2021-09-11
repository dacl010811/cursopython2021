# Estructuras de elementos ordenados
# Operaciones : Añadir elementos
#               Sacar elementos
#  LIFO - (Last in First Out) : El ultimo elemento entrar es el primero en salir

pila = [1,2,3]
pila.append(6) # Agregando al final
print(pila)

pila.append(8) # Agregando al final
print(pila)

# metodo pop() 1
print (pila.pop())
print (pila)

# metodo pop() 2
print (pila.pop())
print (pila)

# metodo pop() 3
print (pila.pop())
print (pila)

print(type(pila))

#Iterar

pila_1 = [1,2,3]
pila_1.append(85)
pila_1.append(86)
pila_1.append(87)


print("Inicial",pila_1)
try:
    for num in range(0,11):
        pila_1.pop()
except IndexError:
    print("Error")
except Exception as e:
    print("Error", type(e).__name__)

print("Final",pila_1)








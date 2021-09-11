#FIFO (First In First Out)
from collections import  deque

#Colas por defecto
cola = deque()
print(cola)
print(type(cola))

# Colas con valores
cola = deque(['Hola','Mundo','Python'])
print(cola)
print(type(cola))

#Agregar elementos a la cola
cola.append('Linux')
print(cola)

cola.append(0)
print(cola)

cola.append(True)
print(cola)

#Sacar los elementos de la cola
#cola.popleft()
#print(cola)

try:
    for num in range(0,11):
        print(cola.popleft())
except IndexError:
    print("Error")
except Exception as e:
    print("Error", type(e).__name__)

print(cola)


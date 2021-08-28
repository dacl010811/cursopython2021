# Esto debe ser el resultado
matriz = [
    [1,1,1,3], #0
    [2,2,2,7], #1
    [3,3,3,9], #2
    [4,4,4,13] #3
]

#Pistas [][:-1]   y  la funcion  sum() build-in  o sumar elemento + elemento
#iterables :   Listas [], Tuplas (), diccionarios {0:"valor"}

matriz[0][-1] = sum(matriz[0][:-1])   # Esto "matriz[0][:-1]" --->> representa a una sub_lista. (Super clase Iterable)
matriz[1][-1] = sum(matriz[1][:-1])
matriz[2][-1] = sum(matriz[2][:-1])
matriz[3][-1] = sum(matriz[3][:-1])

print(f"{matriz[0]}\n")
print(f"{matriz[1]}\n")
print(f"{matriz[2]}\n")
print(f"{matriz[3]}\n")

#Mensaje original encriptado:  "zereP nauJ, 01"
# Resultado : "Juan Perez"  ha sacado un  "10"  de nota.   
# Pistas :   [0:-1] :  [0:-1:2]  :  [::-1]
encriptado = "zereP nauJ, 01"
cadena_desencriptada = encriptado[::-1]

print("Mensaje desencriptado")
print(f"{cadena_desencriptada}")
print(list(cadena_desencriptada))





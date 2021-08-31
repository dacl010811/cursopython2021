#Expresiones Anidadas.
a = 10  # int
b = 5   # int
resultado = ( (10 * 5 - 2**5 >= 20 and not (a % b)) != 0)
resultado = ( (50 - 32 >= 20 and not (False)) != 0)
resultado = ( (18 >= 20 and not (False)) != 0)
resultado = ( (False and not (False)) != 0)
resultado = ( (False and True) != 0)
resultado = ( (False) != 0)
print(resultado)


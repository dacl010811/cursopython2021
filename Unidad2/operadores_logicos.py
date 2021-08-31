#Operadores Logicos

# not :  Negacion Logica

bandera =  not True
print(bandera)

bandera =  not False
print(bandera)


# Conjuncion :  AND  :  Tabla de Verdad

bandera =  True and True  # Verdadera
bandera =  True and False
bandera =  False and True
bandera =  False and False

print(bandera)

# Disyuncion :  OR  :  Tabla de Verdad


bandera =  True or False # Verdadera
bandera =  False or True # Verdadera
bandera =  False or False # False
bandera =  True or (not (not (True or True)))  # Verdadera

print(bandera)










import pickle

lista_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#Crear ficheros
archivo_encriptado = open('datos.dat','wb')
pickle.dump(lista_1,archivo_encriptado)
archivo_encriptado.close()


#Crear ficheros
archivo_encriptado = open('datos.txt','rb')
datos_originales = pickle.load(archivo_encriptado)
archivo_encriptado.close()

print('Datos Originales')
print(datos_originales)



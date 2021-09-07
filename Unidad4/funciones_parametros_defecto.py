#Parametros por defecto.

def resta(a=None,b=None):

    if a != None and b != None:
        if isinstance(a,int) and isinstance(b,int):
            resultado = a-b
        else:
            print("Error, no se pueden realizar operacion con datos que no sean Base10")
            return
    else:
        print("Los datos enviados son nulos")

    return resultado


#Incovacion
r = resta(10,'A')
print("El resultado es :", r)

#variable = 10
#print(type(variable) )
#resultado_validacion = isinstance(variable, int)

#print(resultado_validacion)

"""a = '10a'
cadena_1 = None
for car in (list(a)):
    if isinstance(car,str):
        try:
            numerico = int(car)
        except:
            print("No pudo realizar el castin")
        finally:
            cadena_1 += numerico"""

def convertir():
    a = '10a'
    cadena_1 = ''
    lista_num = []

    for car in (list(a)):    # Lista ['1','0','a']
        if isinstance(car,str):
            try:
                print(type(car))
                numerico = int(car)
                lista_num.append(numerico)
            except:
                print("No pudo realizar el castin")

    print("Mi numero es ", str(lista_num))

convertir()



